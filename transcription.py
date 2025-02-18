import os 
from groq import Groq
import io

groq = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def get_transcription(file: io.BytesIO):
    transcipt = groq.audio.transcriptions.create(
        file=file, model="whisper-large-v3-turbo",
        response_format="json",
        language="en"
        )
    return transcipt