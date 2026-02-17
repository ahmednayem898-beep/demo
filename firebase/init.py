import firebase_admin
from firebase_admin import credentials, firestore
import os
cred = credentials.Certificate({
    "type": "service_account",
    "project_id": os.environ["FIREBASE_PROJECT_ID"],
    "private_key": os.environ["FIREBASE_PRIVATE_KEY"].replace("\\n", "\n"),
    "client_email": os.environ["FIREBASE_CLIENT_EMAIL"],
    "token_uri": os.environ["FIREBASE_CLIENT_URL"] 
})
firebase_admin.initialize_app(cred)
db = firestore.client()


