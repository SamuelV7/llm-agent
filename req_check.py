import os 
from groq import Groq
from pydantic import BaseModel
from typing import List
import json

class TranscriptCheckResult(BaseModel):
    missing_items: List[str]
    violations: List[str]
    met_requirements: List[str]
    ideas_to_improve: List[str]


groq = Groq(api_key=os.environ.get("GROQ_API_KEY"))
requirements = {
    "brand_safety_guidelines": [
        "No explicit adult themes or imagery",
        "No polarizing political topics",
        "No personal attacks or targeted harassment",
        "No unverified theories presented as facts"
    ],
    "must_mention": [
        "Milanote is a tool for organizing creative projects",
        "Sign up for free with no time-limit"
    ],
    "should_highlight": [
        "How Milanote can be used for visual, creative work",
        "At least two example boards (e.g., Moodboard, Project Plan)",
        "Collaborating or sharing boards with others"
    ],
    "avoid": [
        "YouTube-focused planning (e.g., thumbnails, upload schedule)",
        "Skipping an introduction to Milanote",
        "Rushing through without any genuine demonstration",
        "Using the word 'download' instead of 'sign up'"
    ],
    "call_to_action": [
        "Encourage viewers to sign up for Milanote using a unique link",
        "Add a pinned comment with the free signup link",
        "Mention 'milanote' and 'milanoteapp' in tags if applicable"
    ]
}

print(requirements)

def verify_transcript(transcript: str) -> TranscriptCheckResult:
    """
    Sends the transcript and requirements to GROQ,
    instructs it to respond with JSON that fits the TranscriptCheckResult schema.
    Parses and returns a TranscriptCheckResult object.
    """

    # 1) System instructions
    system_instructions = """\
    You are a helpful assistant that evaluates transcripts against marketing requirements.
    Return ONLY valid JSON that matches the schema:
    {
    "missing_items": [],
    "violations": [],
    "met_requirements": []
    "ideas_to_improve": []
    }

    - Do not include extra fields or markdown formatting.
    - "missing_items": Items that were required/expected but not found in the transcript
    - "violations": Any brand safety or 'avoid' issues found in the transcript
    - "met_requirements": Requirements that the transcript successfully fulfilled
    - "ideas_to_improve" : Things that can be improved upon given the requirement criteria
    """

    # 2) Combine the requirements + transcript into a single user message
    user_content = f"""
    REQUIREMENTS:
    {json.dumps(requirements, indent=2)}

    TRANSCRIPT:
    {transcript}
    """

    # 3) Call the ChatCompletion API
    response = groq.chat.completions.create(
        model="deepseek-r1-distill-llama-70b",
        messages=[
            {"role": "system", "content": system_instructions},
            {"role": "user", "content": user_content},
        ],
        temperature=0.6,
        # max_tokens=6000,
        max_completion_tokens=4096,
        top_p=0.95,
    )

    # 4) Extract groq's message content (should be JSON)
    groq_reply = response.choices[0].message.content.strip()

    # 5) Parse JSON into Python dict
    try:
        # Deep Seek R1 has <think> tags
        groq_json = groq_reply.split("think>")[2].split("json\n")[1].split("```")[0]
        result_dict = json.loads(groq_json)
        print(f"Response {result_dict}")
    except json.JSONDecodeError as e:
        raise ValueError(f"Groq response was not valid JSON:\n{groq_reply}\nError: {e}")

    # 6) Parse that dict into a TranscriptCheckResult via Pydantic
    try:
        validated_result = TranscriptCheckResult(**result_dict)
    except Exception as e:
        raise ValueError(f"Groq response JSON didn't match the Pydantic schema:\n{groq_reply}\nError: {e}")

    return validated_result
