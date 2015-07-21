import requests,json, sys, traceback
from datetime import datetime
from decimal import Decimal

def apply_format(value):
    return format(Decimal(value),'.5f')

def apply_format_level(value):
    return format(Decimal(value),'.2f')

def get_datetime():
    return datetime.now().strftime('%Y-%m-%d %h:%m:%s')

def get_timestamp():
    return time.mktime(time.gmtime())

def get_response(url,ccy,body=None,params=None):
    #print "URL ", url 
    #print "CCY ", ccy 
    #print "BODY ", body 
    guard(url, ccy)
    if ccy:
       url = url % ccy 
    if params:
       url = "%s%s" % (url,params) 
    try:
        if body:
            data = json.loads(body)
            response = requests.post(url,json=data)
        else:
            response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print "Exception in API request %s : %s " % (url, e)
        print '-'*60
        traceback.print_exc(file=sys.stdout)
        print '-'*60

def guard(url,ccy):
    if ccy:
       if '%' not in url: # should have slot for the currency in URL
         raise ValueError("URL %s does not have a '%' for adding currency value supplied" % (url,ccy))
    else:
       if '%' in url: # should have ccy to pass via URL
         raise ValueError("URL %s should have a currency value supplied" % url)
