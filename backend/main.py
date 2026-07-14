"""AI SaaS Starter - Main Application."""

from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from auth import get_current_user
from billing import check_subscription
from usage import track_usage
from ai import chat_with_ai

app = FastAPI(
    title="AI SaaS Starter",
    description="Production-ready SaaS with AI integration",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "AI SaaS Starter API", "version": "1.0.0"}

@app.get("/health")
async def health():
    return {"status": "healthy"}

@app.post("/api/ai/chat")
async def ai_chat(
    message: str,
    user = Depends(get_current_user),
    subscription = Depends(check_subscription)
):
    """Chat with AI."""
    if not subscription["active"]:
        raise HTTPException(403, "Subscription required")
    
    track_usage(user["id"], "chat")
    response = await chat_with_ai(message, user["id"])
    return {"response": response}

@app.get("/api/usage")
async def get_usage(user = Depends(get_current_user)):
    """Get user usage stats."""
    from usage import get_usage_stats
    return get_usage_stats(user["id"])

@app.get("/api/billing/portal")
async def billing_portal(user = Depends(get_current_user)):
    """Get Stripe billing portal URL."""
    from billing import create_portal_session
    return await create_portal_session(user["id"])
