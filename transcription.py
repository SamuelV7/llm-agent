import os 
from groq import Groq
from pydantic import BaseModel
from typing import List
import json
import io

groq = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def get_transcription(file: io.BytesIO):
    groq.audio.transcriptions.create(file=file, model="whisper-large-v3-turbo")