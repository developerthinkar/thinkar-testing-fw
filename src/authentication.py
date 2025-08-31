from office365.runtime.auth.user_credential import UserCredential
from office365.sharepoint.client_context import ClientContext
from dotenv import load_dotenv
import os

load_dotenv()

USERNAME = os.getenv("SP_USERNAME")
PASSWORD = os.getenv("SP_PASSWORD")

SITE_URL = "https://axionsolutions.sharepoint.com/sites/ProjectDeliverySupport"

CTX = ClientContext(SITE_URL).with_credentials(UserCredential(USERNAME, PASSWORD))



# App Registration 
# from office365.sharepoint.client_context import ClientContext
# from office365.runtime.auth.client_credential import ClientCredential

# CLIENT_ID = ""
# CLIENT_SECRET = ""  # Your secret ID
# SITE_URL = "https://axionsolutions.sharepoint.com/sites/Think-AR-DOCS"

# # Create authentication credentials
# credentials = ClientCredential(CLIENT_ID, CLIENT_SECRET)

# # Create SharePoint context with app registration
# CTX = ClientContext(SITE_URL).with_credentials(credentials)