from txt.prompt import promptBuilder
from firebase.base import *
from tools.request import req_prompt
from handlers.doc.process.controller import controller
import json
def parseJson(strL):
    try:
        return {
            "data":json.loads(strL),
            "success":True
        }
    except:
        return {
            "msg":strL,
            "success":False,
        }

def ask_doc(qus):
    finalPrompt = promptBuilder(qus)
    finalresult = req_prompt(finalPrompt)
    if finalresult['success']:
        result  = parseJson(finalresult['text'])
        final_result  = controller(result)
        return final_result
    else:
        return parseJson(finalresult['error'][0]['msg'])
    
