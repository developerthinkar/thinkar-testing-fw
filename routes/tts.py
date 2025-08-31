# routes/tts.py
import io
import wave
from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from openai import AsyncOpenAI
from dotenv import load_dotenv
import os

router = APIRouter()

# Load env
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Init OpenAI client
openai = AsyncOpenAI(api_key=OPENAI_API_KEY)

# Request schema
class TextRequest(BaseModel):
    text: str

async def text_to_wav_bytes(text: str) -> bytes:
    buffer = io.BytesIO()

    async with openai.audio.speech.with_streaming_response.create(
        model="gpt-4o-mini-tts",
        voice="coral",
        input=text,
        response_format="pcm",
    ) as response:
        with wave.open(buffer, "wb") as wav_file:
            wav_file.setnchannels(1)      # mono
            wav_file.setsampwidth(2)      # 16-bit
            wav_file.setframerate(24000)  # 24 kHz
            async for chunk in response.iter_bytes():
                wav_file.writeframes(chunk)

    buffer.seek(0)
    return buffer.read()


@router.post("/text-to-wav")
async def text_to_wav_endpoint(data: TextRequest):
    wav_bytes = await text_to_wav_bytes(data.text)
    return StreamingResponse(
        io.BytesIO(wav_bytes),
        media_type="audio/wav",
        headers={
            "Content-Disposition": 'attachment; filename="output.wav"'
        },
    )
