import requests,json
from datetime import datetime
from decimal import Decimal

def apply_format(value):
    return format(Decimal(value),'.5f')

def apply_format_level(value):
    return format(Decimal(value),'.2f')

def get_datetime():
    return datetime.now().strftime('%Y-%m-%d %h:%m:%s')

def get_response(url,ccy,body=None):
    guard(url, ccy)
    if ccy:
       url = url % ccy 
    try:
        if body:
            data = json.loads(body)
            response = requests.post(url,json=data)
        else:
            response = requests.get(url)
        response.raise_for_status()
        json_response = response.json()
        return json_response
    except Exception as e:
        raise Exception('API request rejected: %s' % str(e))

def guard(url,ccy):
    if ccy:
       if '%' not in url: # should have slot for the currency in URL
         raise ValueError("URL %s does not have a '%' for adding currency value supplied" % (url,ccy))
    else:
       if '%' in url: # should have ccy to pass via URL
         raise ValueError("URL %s should have a currency value supplied" % url)
