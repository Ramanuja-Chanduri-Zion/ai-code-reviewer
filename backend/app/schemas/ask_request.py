from pydantic import BaseModel, Field

class AskRequest(BaseModel):
    """Input schema for the ask endpoint."""
    question: str = Field(..., description="The question to ask the model.")
    context: str = Field(..., description="The context to provide to the model.")
    
    # temperature: float = Field(1.0, description="Sampling temperature.")
    # max_tokens: int = Field(100, description="Maximum number of tokens to generate.")
    # top_p: float = Field(1.0, description="Nucleus sampling parameter.")
    # frequency_penalty: float = Field(0.0, description="Frequency penalty for token generation.")
    # presence_penalty: float = Field(0.0, description="Presence penalty for token generation.")
    # stop: list[str] = Field([], description="List of stop sequences for token generation.")