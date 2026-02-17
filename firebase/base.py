from firebase.init import db
def save(doc={}):
    try:
        if len(doc) <=2 :
            return False
        if doc['authname'] == None or doc['topic'] == None  :
            return False
        doc_ref = db.collection(doc['topic']).document(doc['authname'])
        doc_ref.set(doc)
        print("Data added successfully!")
        return True
    except:
        return False


def getAll():
    collection_ref = db.collection("mavr")
    docs = collection_ref.stream()
    return {doc.id: doc.to_dict() for doc in docs}


def getOne(params):
    authname = params.get('authname')
    topic = params.get('topic')

    if not authname or not topic:
        return None

    collection_ref = db.collection(topic)
    query = collection_ref.where("authname", "==", authname)
    results = query.stream()
    for doc in results:
        return {
            "success": True,
            "data": doc.to_dict()
        }
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


def deleteD_by_authname(params):
    authname = params.get('authname')
    topic = params.get('topic')
    if not authname or not topic:
        return False
    collection_ref = db.collection(topic)
    query = collection_ref.where("authname", "==", authname)
    results = query.stream()

    deleted_count = 0
    for doc in results:
        doc.reference.delete()
        deleted_count += 1

    if deleted_count > 0:
        return True
    else:
        return True
