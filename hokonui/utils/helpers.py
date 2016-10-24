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

def get_response(url,ccy,params=None,body=None):
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

def get_orders(data,max_qty,bids_tag,asks_tag,price_tag=0,qty_tag=1):
    orders = {}
    bids = {}
    asks = {}
    buyMax = 0
    sellMax = 0
    for level in data[bids_tag]:
        if buyMax > max_qty:
            continue
        else:
            bids[apply_format_level(level[price_tag])] = "{:.8f}".format(float(level[qty_tag]))
        buyMax = buyMax + float(level[qty_tag])

    for level in data[asks_tag]:
        if sellMax > max_qty:
            continue
        else:
            asks[apply_format_level(level[price_tag])] = "{:.8f}".format(float(level[qty_tag]))
        sellMax = sellMax + float(level[qty_tag])
    orders["source"] = "ITBIT"
    orders["bids"] = bids
    orders["asks"] = asks
    orders["timestamp"] = str(int(time.time()))
    return orders

def guard(url,ccy):
    if ccy:
       if '%' not in url: # should have slot for the currency in URL
         raise ValueError("URL %s does not have a '%' for adding currency value supplied" % (url,ccy))
    else:
       if '%' in url: # should have ccy to pass via URL
         raise ValueError("URL %s should have a currency value supplied" % url)
