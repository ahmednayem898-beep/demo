from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import os
import requests

app = FastAPI()

# BOT_TOKEN = os.getenv("DC_token")
# WEBHOOK_URL = os.getenv("discord_urls")
@app.get("/")
async def test(req: Request):
    return {
        "success":True
    }
# @app.post("/interactions")
# async def interactions(req: Request):
#     data = await req.json()
    
#     if data.get("type") == 1:
#         return JSONResponse({"type": 1})

#     if data.get("data", {}).get("name") == "ask":
#         question = data["data"]["options"][0]["value"]
        
#         answer = f"Demo response to: {question}"

#         requests.patch(
#             WEBHOOK_URL,
#             json={"content": answer},
#             headers={"Authorization": f"Bot {BOT_TOKEN}"}
#         )

#         return JSONResponse({"type": 5})
    
#     return JSONResponse({"error": "Unknown command"}, status_code=400)
