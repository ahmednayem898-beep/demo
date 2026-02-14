from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import os
import httpx

app = FastAPI()

BOT_TOKEN = os.getenv("DC_token")          
WEBHOOK_URL = os.getenv("discord_urls")    


@app.get("/")
async def root():
    return {"status": "FastAPI Discord Bot Running 🚀"}


@app.post("/interactions")
async def interactions(req: Request):
    try:
        data = await req.json()
    except Exception:
        return JSONResponse({"error": "Invalid JSON"}, status_code=400)

    if data.get("type") == 1:
        return JSONResponse({"type": 1})

    if data.get("type") == 2: 

        command_name = data.get("data", {}).get("name")

        if command_name == "ask":
            question = data["data"]["options"][0]["value"]

            answer = f"Demo response to: {question}"

            async with httpx.AsyncClient() as client:
                await client.patch(
                    WEBHOOK_URL,
                    json={"content": answer},
                    headers={"Authorization": f"Bot {BOT_TOKEN}"}
                )

            return JSONResponse({
                "type": 5 
            })

    return JSONResponse({"error": "Unknown interaction"}, status_code=400)
