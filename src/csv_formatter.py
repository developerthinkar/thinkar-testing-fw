import pandas as pd
from src import tool_description
import json

def process_uploaded_csv(df):
    """
    Process the uploaded CSV with transformations from process_csv function
    
    Args:
        df: Input DataFrame
        
    Returns:
        processed DataFrame
    """
    # Make a copy to avoid modifying the original
    processed_df = df.copy()
    
    # 1. Create "Date" column from "Timestamp" (if Timestamp column exists)
    if "Timestamp" in processed_df.columns:
        processed_df["Date"] = pd.to_datetime(processed_df["Timestamp"]).dt.date
    
    # 2. Mapping dictionary for tool call names
    tool_call_map = {
        "thinkar_device_tool_battery": "Battery",
        "thinkar_device_tool_brightness": "Brightness",
        "thinkar_device_tool_dnd": "Do Not Disturb",
        "thinkar_device_tool_language": "Language",
        "thinkar_device_tool_page_compass": "Compass",
        "thinkar_device_tool_page_navigation": "Navigation",
        "thinkar_device_tool_page_take_AI_photo": "Take Ai Photo",
        "thinkar_device_tool_page_take_photo": "Take Photo",
        "thinkar_device_tool_page_take_video": "Take Video",
        "thinkar_device_tool_page_teleprompter": "Teleprompter",
        "thinkar_device_tool_page_translation": "Translation",
        "thinkar_device_tool_screen_mode": "Screen Mode",
        "thinkar_device_tool_version": "Version",
        "thinkar_device_tool_volume": "Volume",
        "thinkar_device_tool_widget_health": "Health",
        "thinkar_device_tool_widget_news": "News",
        "thinkar_device_tool_widget_point_of_interest": "Point of Interest",
        "thinkar_device_tool_widget_sports": "Sports",
        "thinkar_device_tool_widget_stock_ticker": "Stock Ticker",
        "thinkar_device_tool_widget_weather": "Weather"
    }

    # 3. Build tool_description_map dynamically from tool_description.py
    tool_description_map = {
        getattr(tool_description, attr)["name"]: getattr(tool_description, attr)
        for attr in dir(tool_description)
        if not attr.startswith("__") and isinstance(getattr(tool_description, attr), dict)
    }

    # 4. Map Expected Tool Call → Tool Call Name + Tool Description (if Expected Tool Call column exists)
    if "Expected Tool Call" in processed_df.columns:
        processed_df["Tool Call Name"] = processed_df["Expected Tool Call"].map(tool_call_map)
        
        # Store the full dict as JSON string
        processed_df["Tool Description"] = processed_df["Expected Tool Call"].map(
            lambda x: json.dumps(tool_description_map.get(x, {}), ensure_ascii=False, indent=4)
        )
    
    return processed_df