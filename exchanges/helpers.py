import requests,json
from datetime import datetime
from decimal import Decimal

def apply_format(value):
    return format(Decimal(value),'.5f')

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
