from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import os

app = FastAPI()

# Example environment variable usage
# GREETING = os.getenv("GREETING", "Hello from FastAPI on Vercel!")

@app.get("/")
async def root():
    return {"message": "Hello from FastAPI on Vercel!"}

@app.post("/echo")
async def echo(request: Request):
    data = await request.json()
    return {"received": data}
