
from fastapi import FastAPI
from routes import search, chatbot

app = FastAPI(title="CyberLaw AI Backend", version="1.0")

app.include_router(search.router, prefix="/search", tags=["Search"])
app.include_router(chatbot.router, prefix="/chatbot", tags=["Chatbot"])

@app.get("/")
def root():
    return {"message": "CyberLaw API is running."}
