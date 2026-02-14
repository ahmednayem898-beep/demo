from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
import os
import httpx
from nacl.signing import VerifyKey
from nacl.exceptions import BadSignatureError

app = FastAPI()

# 🔐 Your Discord Public Key
PUBLIC_KEY = "0a3c6bd24979b246a43f1ec0976af100579d8005c5ee2592e3eeff2baddae295"

BOT_TOKEN = os.getenv("DC_token")
WEBHOOK_URL = os.getenv("discord_urls")


def verify_signature(request: Request, body: bytes):
    signature = request.headers.get("X-Signature-Ed25519")
    timestamp = request.headers.get("X-Signature-Timestamp")

    if not signature or not timestamp:
        raise HTTPException(status_code=401, detail="Missing signature headers")

    verify_key = VerifyKey(bytes.fromhex(PUBLIC_KEY))

    try:
        verify_key.verify(timestamp.encode() + body, bytes.fromhex(signature))
    except BadSignatureError:
        raise HTTPException(status_code=401, detail="Invalid request signature")


@app.get("/")
async def root():
    return {"status": "Discord FastAPI Bot Running 🚀"}


@app.post("/interactions")
async def interactions(request: Request):
    body = await request.body()

    # ✅ REQUIRED by Discord
    verify_signature(request, body)

    data = await request.json()

    # 🔁 Discord PING
    if data.get("type") == 1:
        return JSONResponse({"type": 1})

    # 💬 Slash command
    if data.get("type") == 2:
        command_name = data.get("data", {}).get("name")

        if command_name == "ask":
            question = data["data"]["options"][0]["value"]
            answer = f"Demo response to: {question}"

            # Send follow-up message
            async with httpx.AsyncClient() as client:
                await client.patch(
                    WEBHOOK_URL,
                    json={"content": answer},
                    headers={"Authorization": f"Bot {BOT_TOKEN}"}
                )

            return JSONResponse({"type": 5})

    return JSONResponse({"error": "Unknown interaction"}, status_code=400)
