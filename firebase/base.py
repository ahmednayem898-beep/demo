import firebase_admin
from firebase_admin import credentials, firestore
import os
cred = credentials.Certificate({
    "type": "service_account",
    "project_id": os.environ["FIREBASE_PROJECT_ID"],
    "private_key": os.environ["FIREBASE_PRIVATE_KEY"].replace("\\n", "\n"),
    "client_email": os.environ["FIREBASE_CLIENT_EMAIL"],
    "token_uri": "https://oauth2.googleapis.com/token"
})

firebase_admin.initialize_app(cred)
db = firestore.client()


def save(doc={}):
    doc_ref = db.collection("mavr").document("ets2")
    doc_ref.set(doc)
    print("Data added successfully!")


def getAll():
    collection_ref = db.collection("mavr")
    docs = collection_ref.stream()
    return {doc.id: doc.to_dict() for doc in docs}


def getOne(doc_id):
    doc_ref = db.collection("mavr").document(doc_id)
    doc = doc_ref.get()
    if doc.exists:
        return doc.to_dict()
    return None


def getMany(doc_ids):
    result = {}
    for doc_id in doc_ids:
        doc_ref = db.collection("mavr").document(doc_id)
        doc = doc_ref.get()
        if doc.exists:
            result[doc_id] = doc.to_dict()
    return result


def updateD(doc_id, update_data):
    doc_ref = db.collection("mavr").document(doc_id)
    doc_ref.update(update_data)
    print(f"Document {doc_id} updated successfully!")


def deleteD(doc_id):
    doc_ref = db.collection("mavr").document(doc_id)
    doc_ref.delete()
    print(f"Document {doc_id} deleted successfully!")


