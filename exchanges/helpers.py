import requests,json
from datetime import datetime

def get_datetime():
    return datetime.now().strftime('%Y-%m-%d %h:%m:%s')

def get_response(url,body=None):
    if body:
        data = json.loads(body)
        response = requests.post(url,json=data)
    else:
        response = requests.get(url)
    response.raise_for_status()
    return response.json()
