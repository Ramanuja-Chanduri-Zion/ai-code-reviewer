import logging
from google import genai
from google.genai import types
from schemas import AskRequest
from fastapi import APIRouter, HTTPException, Depends
from config import CONTENT_CONFIG, PROJECT_NAME, PROJECT_LOCATION, MODEL_NAME
from typing import Dict, Any

logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/genai",
    tags=["requests"],
    responses={404: {"description": "Not found"}},
)

@router.post("/ask")
def ask(request: AskRequest) -> Dict[str, Any]:
    """
    Generate a response from the model based on the user's question.
    """
    try:
        # Initialize the GenAI client
        client = genai.Client(
            vertexai=True,
            project=PROJECT_NAME,
            location=PROJECT_LOCATION,
        )

        prompt = f"""
        You are a helpful assistant. Answer the question based on the context provided.
        If the question is not answerable, say "I don't know".
        Context: {request.context}
        Question: {request.question}
        """

        # Prepare the model and content
        model = MODEL_NAME
        contents = [
            types.Content(
                role="user",
                parts=[
                    types.Part.from_text(text=prompt)
                ]
            )
        ]

        response = ""

        # Generate content using the model
        for chunk in client.models.generate_content_stream(
            model=model,
            contents=contents,
            config=CONTENT_CONFIG,
        ): 
            response += chunk.text

        logger.info(f"Generated response: {response}")
        
        # Return the generated response
        return {
            "response": response,
            "status": "success"
        }


    except Exception as e:
        logger.error(f"Error generating content: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")