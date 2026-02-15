from ai_support import req_prompt
from txt.prompt import prompt as prePrompt
def ask_res(qus):
    final_prompt = f"""
    {prePrompt}
    Question:{qus}
    """
    response  = req_prompt(final_prompt)
    if response['success']:
        return {
            "msg": response['text']
        }
    else:
        return {
            "msg": response['error'][0]['msg']
        } 