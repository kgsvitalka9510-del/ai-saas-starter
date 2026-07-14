"""Stripe billing integration."""

import stripe
from fastapi import HTTPException

stripe.api_key = "sk_test_your_stripe_key"

PLANS = {
    "free": {"price": 0, "requests": 1000},
    "pro": {"price": 2900, "requests": -1},
    "enterprise": {"price": 9900, "requests": -1},
}

async def create_checkout_session(user_id: str, plan: str):
    if plan not in PLANS:
        raise HTTPException(400, "Invalid plan")
    
    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=[{
            "price_data": {
                "currency": "usd",
                "product_data": {"name": f"AI SaaS - {plan.title()}"},
                "unit_amount": PLANS[plan]["price"],
            },
            "quantity": 1,
        }],
        mode="payment",
        success_url="https://example.com/success",
        cancel_url="https://example.com/cancel",
        metadata={"user_id": user_id, "plan": plan},
    )
    return {"checkout_url": session.url}

async def check_subscription(user_id: str) -> dict:
    return {"active": True, "plan": "free", "requests_remaining": 999}
