import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.tts import router as tts_router
from routes.sharepoint_uploader import router as sharepoint_uploader_router

app = FastAPI(
    title="ThinkAR Testing Automation",
    description="",
    version="0.1.0",
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routers
app.include_router(tts_router, tags=["TTS"])  
app.include_router(sharepoint_uploader_router, tags=["SharePoint File Upload"])


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
