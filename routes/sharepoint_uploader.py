import io
import pandas as pd
import json
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from office365.sharepoint.files.file import File as SharePointFile
from office365.runtime.client_request_exception import ClientRequestException
from src.authentication import CTX
from src.csv_formatter import process_uploaded_csv
from fastapi import APIRouter

router = APIRouter()

# SharePoint configuration
TARGET_URL = "/sites/ProjectDeliverySupport/Shared Documents/Software Projects/ThinkAR/ThinkAR - Test Results"
CSV_FILENAME = "thinkar_test_results.csv"

def check_file_exists_in_sharepoint(file_url):
    """
    Check if a file exists in SharePoint
    
    Args:
        file_url: Full path to the file in SharePoint
        
    Returns:
        bool: True if file exists, False otherwise
    """
    try:
        file = CTX.web.get_file_by_server_relative_url(file_url)
        CTX.load(file)
        CTX.execute_query()
        return True
    except ClientRequestException as e:
        if "File Not Found" in str(e) or "404" in str(e):
            return False
        else:
            raise e

def create_initial_csv_file(df_sample, filename, target_url):
    """
    Create an initial CSV file in SharePoint using the structure of the uploaded file
    
    Args:
        df_sample: Sample DataFrame to get column structure
        filename: Name of the CSV file
        target_url: SharePoint folder URL
    """
    # Create empty DataFrame with same columns
    empty_df = pd.DataFrame(columns=df_sample.columns)
    direct_upload_to_sharepoint_as_csv(empty_df, filename, target_url)
    print(f"Created initial empty CSV file: {filename}")

def direct_upload_to_sharepoint_as_csv(df, filename, target_url):
    """Upload DataFrame as CSV to SharePoint"""
    csv_obj = io.StringIO()
    df.to_csv(csv_obj, index=False)
    csv_obj.seek(0)
    bytes_obj = io.BytesIO(csv_obj.getvalue().encode())
    target_folder = CTX.web.get_folder_by_server_relative_url(target_url)
    target_file = target_folder.upload_file(filename, bytes_obj)
    CTX.execute_query()
    print(filename, "has been uploaded to url:", target_file.serverRelativeUrl)

def download_from_sharepoint_as_csv(file_url):
    """Download CSV from SharePoint and return as DataFrame"""
    response = SharePointFile.open_binary(CTX, file_url)
    bytes_file_obj = io.BytesIO()
    bytes_file_obj.write(response.content)
    bytes_file_obj.seek(0)
    csv_obj = io.StringIO(bytes_file_obj.getvalue().decode())
    df = pd.read_csv(csv_obj)
    return df

def add_rows_to_sharepoint_csv(file_url, new_rows, target_url, filename):
    """Add new rows to existing SharePoint CSV"""
    # Download existing file
    existing_df = download_from_sharepoint_as_csv(file_url)
    print(f"Downloaded existing file with {len(existing_df)} rows")
    
    # Convert new_rows to DataFrame if it's a list of dictionaries
    if isinstance(new_rows, list):
        new_df = pd.DataFrame(new_rows)
    else:
        new_df = new_rows
    
    # Combine existing data with new rows
    updated_df = pd.concat([existing_df, new_df], ignore_index=True)
    print(f"Added {len(new_df)} new rows. Total rows: {len(updated_df)}")
    
    # Upload the updated file
    direct_upload_to_sharepoint_as_csv(updated_df, filename, target_url)
    
    return updated_df


@router.post("/sharepoint_uploader/")
async def upload_test_results(file: UploadFile = File(...)):
    """
    Upload a CSV file, process it with transformations, and append to SharePoint
    
    Args:
        file: Uploaded CSV file
        
    Returns:
        JSON response with success message and file details
    """
    try:
        # Validate file type
        if not file.filename.endswith('.csv'):
            raise HTTPException(status_code=400, detail="Only CSV files are allowed")
        
        # Read uploaded file
        contents = await file.read()
        csv_obj = io.StringIO(contents.decode('utf-8'))
        uploaded_df = pd.read_csv(csv_obj)
        
        if uploaded_df.empty:
            raise HTTPException(status_code=400, detail="Uploaded file is empty")
        
        print(f"Received file: {file.filename} with {len(uploaded_df)} rows")
        print(f"Original columns: {list(uploaded_df.columns)}")
        
        # PROCESS THE CSV WITH TRANSFORMATIONS
        processed_df = process_uploaded_csv(uploaded_df)
        print(f"Processed columns: {list(processed_df.columns)}")
        
        # Full path to the target CSV file in SharePoint
        target_file_url = f"{TARGET_URL}/{CSV_FILENAME}"
        
        # Check if thinkar_test_results.csv exists
        file_exists = check_file_exists_in_sharepoint(target_file_url)
        
        if not file_exists:
            # Create initial file with the structure of processed file
            print(f"File {CSV_FILENAME} does not exist. Creating new file...")
            create_initial_csv_file(processed_df, CSV_FILENAME, TARGET_URL)
            
            # Now add the processed data
            updated_df = add_rows_to_sharepoint_csv(
                file_url=target_file_url,
                new_rows=processed_df,
                target_url=TARGET_URL,
                filename=CSV_FILENAME
            )
        else:
            # File exists, append processed data
            print(f"File {CSV_FILENAME} exists. Appending processed data...")
            updated_df = add_rows_to_sharepoint_csv(
                file_url=target_file_url,
                new_rows=processed_df,
                target_url=TARGET_URL,
                filename=CSV_FILENAME
            )
        
        # Prepare response with information about transformations
        transformations_applied = []
        if "Timestamp" in uploaded_df.columns and "Date" in processed_df.columns:
            transformations_applied.append("Created Date column from Timestamp")
        if "Expected Tool Call" in uploaded_df.columns:
            if "Tool Call Name" in processed_df.columns:
                transformations_applied.append("Added Tool Call Name mappings")
            if "Tool Description" in processed_df.columns:
                transformations_applied.append("Added Tool Description JSON data")
        
        return JSONResponse(
            status_code=200,
            content={
                "message": "File uploaded, processed, and data appended successfully",
                "uploaded_file": file.filename,
                "rows_uploaded": len(uploaded_df),
                "rows_processed": len(processed_df),
                "rows_added": len(processed_df),
                "total_rows_in_sharepoint": len(updated_df),
                "target_file": CSV_FILENAME,
                "sharepoint_url": target_file_url,
                "transformations_applied": transformations_applied,
                "original_columns": list(uploaded_df.columns),
                "processed_columns": list(processed_df.columns)
            }
        )
        
    except pd.errors.EmptyDataError:
        raise HTTPException(status_code=400, detail="The uploaded file is empty or invalid CSV format")
    
    except pd.errors.ParserError as e:
        raise HTTPException(status_code=400, detail=f"Error parsing CSV file: {str(e)}")
    
    except ClientRequestException as e:
        raise HTTPException(status_code=500, detail=f"SharePoint error: {str(e)}")
    
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")


