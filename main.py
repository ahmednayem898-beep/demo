from fastapi import FastAPI, Request
from dotenv import load_dotenv
import os

load_dotenv() 

app = FastAPI()

GREETING = os.getenv("discord_urls", "Hello default!") 

@app.get("/")
async def root():
    return {"message": GREETING}

@app.post("/echo")
async def echo(request: Request):
    data = await request.json()
    return {"received": data}
