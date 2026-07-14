# Setup Guide

## Prerequisites

- Python 3.11+
- Node.js 18+
- Stripe account
- OpenAI API key

## Installation

### Backend

```bash
cd backend
pip install -r requirements.txt
cp .env.example .env
# Edit .env with your keys
uvicorn main:app --reload
```

### Frontend

```bash
cd frontend
npm install
npm start
```

## Configuration

1. Create Stripe account at stripe.com
2. Get API keys from Stripe dashboard
3. Add keys to .env file
4. Create OpenAI account at openai.com
5. Get API key and add to .env

## First Run

1. Visit http://localhost:3000
2. Register an account
3. Start using the AI features
