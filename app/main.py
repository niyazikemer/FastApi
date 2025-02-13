from fastapi import FastAPI
from app.routes import chat

app = FastAPI()

# Include routers
app.include_router(chat.router)