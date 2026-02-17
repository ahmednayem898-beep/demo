from firebase.base import save,deleteD_by_authname,getOne
from handlers.text.message.doc import Doc
def controller(doc_p):
   
    if  doc_p['data']['status'] == 301:
        pass
    elif  doc_p['data']['status'] == 302:
        pass
    elif  doc_p['data']['status'] == 303:
        pass
    elif doc_p['data']['type'] == 1 and doc_p['data']['status'] == 200:
        result  = save(doc_p['data']['answer'])
        if result:
            return {
                "success":True,
                "msg":f"{Doc().getSaveSuccessMsg()}\n topic:{doc_p['data']['answer']['topic']}\n{doc_p['data']['answer']}"
            }
        else:
            return {
                "success":True,
                "msg":Doc().getSaveErrorMsg()
            }

    elif doc_p['data']['type'] == 2 and doc_p['data']['status'] == 200:
        pass
    elif doc_p['data']['type'] == 3 and doc_p['data']['status'] == 200:
        result  = getOne(doc_p['data']['answer'])
        if result:
            return {
                "success":True,
                "msg":result['data']
            }
        else:
            return {
                "success":False,
                "msg":f"{Doc().getFindErrorMsg()}\n topic:{doc_p['data']['answer']['topic']}\n{doc_p['data']['answer']}"
            }
    elif doc_p['data']['type'] == 4 and doc_p['data']['status'] == 200:
        result  = deleteD_by_authname(doc_p['data']['answer'])
        if result:
            return {
                "success":True,
                "msg":f"{Doc().getDeleteMsg()}\n topic:{doc_p['data']['answer']['topic']}\n{doc_p['data']['answer']}"
            }
        else:
            return {
                "success":False,
                "msg":f"{Doc().getDeleteErrorMsg()}\n topic:{doc_p['data']['answer']['topic']}\n{doc_p['data']['answer']}"
            }
    elif doc_p['data']['type'] == 1 and doc_p['data']['status'] == 200:
        pass
    

    