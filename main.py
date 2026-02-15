from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from nacl.signing import VerifyKey
from nacl.exceptions import BadSignatureError
from response.ask.res_1 import ask_res

app = FastAPI()

PUBLIC_KEY = "0a3c6bd24979b246a43f1ec0976af100579d8005c5ee2592e3eeff2baddae295"


def verify_signature(request: Request, body: bytes):
    signature = request.headers.get("X-Signature-Ed25519")
    timestamp = request.headers.get("X-Signature-Timestamp")

    if not signature or not timestamp:
        raise HTTPException(status_code=401, detail="Missing signature headers")

    verify_key = VerifyKey(bytes.fromhex(PUBLIC_KEY))

    try:
        verify_key.verify(timestamp.encode() + body, bytes.fromhex(signature))
    except BadSignatureError:
        raise HTTPException(status_code=401, detail="Invalid signature")






@app.post("/interactions")
async def interactions(request: Request):
    body = await request.body()
    verify_signature(request, body)

    data = await request.json()

    if data.get("type") == 1:
        return JSONResponse({"type": 1})

    if data.get("type") == 2:
        command_name = data["data"]["name"]

        if command_name == "ask":
            question = data["data"]["options"][0]["value"]
            ai_response = ask_res(question)
            return JSONResponse({
                "type": 4,  
                "data": {
                    "content": f"📌 **Your Question:**\n```{question}```\n\n💡 **Answer:**\n{ai_response['msg']}"
                }
            })

    return JSONResponse({"error": "Unknown interaction"}, status_code=400)
