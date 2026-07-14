"""AI integration module."""

import os
from typing import Optional

async def chat_with_ai(message: str, user_id: str) -> str:
    """Chat with OpenAI."""
    # In production, use actual OpenAI API
    api_key = os.getenv("OPENAI_API_KEY")
    
    if not api_key:
        return f"AI response to: {message}"
    
    # TODO: Implement actual OpenAI call
    return f"AI response to: {message}"
