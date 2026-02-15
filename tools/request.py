import requests
import time
import os
def req_prompt(prompt):
    ai_api_key = os.getenv("OPENROUTER_API_KEY")
    ai_api_url = os.getenv("OPENROUTER_API_URL")
    model_name = "gpt-3.5-turbo"  
    max_retries = 5
    for attempt in range(1, max_retries + 1):
        try:
            response = requests.post(
                url=ai_api_url,
                headers={
                    "Authorization": f"Bearer {ai_api_key}"
                },
                json={
                    "model": model_name,
                    "messages": [{"role": "user", "content": prompt}]
                }
            )
            if response.status_code == 200:
                data = response.json()
                ai_text = data['choices'][0]['message']['content']
                return {
                    "text":ai_text,
                    "success":True
                }
            elif response.status_code == 429:
                retry_after = 5  
                print(f"Rate limited (429). Retry attempt {attempt} in {retry_after}s...")
                time.sleep(retry_after)
            else:
                return {
                    "success":False,
                    "error":[{
                        "msg":'Oops! Something went wrong. Please try again.'
                    }]
                }

        except Exception as e:
            return {
                    "success":False,
                    "error":[{
                        "msg":'Oops! Something went wrong. Please try again.'
                    }]
                }
































