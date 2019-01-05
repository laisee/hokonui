''' Module containing helper methods '''

import json
import sys
import traceback
import time
from datetime import datetime
from decimal import Decimal
import requests

def docstring_parameter(*sub):
    def dec(obj):
        obj.__doc__ = obj.__doc__.format(*sub)
        return obj
    return dec

def apply_format(value):
    ''' Method for applying formats '''
    return format(Decimal(value), '.5f')


def apply_format_level(value):
    ''' Method for applying format levels '''
    return format(Decimal(value), '.2f')


def get_datetime():
    ''' Method for generating datetime valsuies '''
    return datetime.now().strftime('%Y-%m-%d %h:%m:%s')


def get_timestamp():
    ''' Method for calculating timestamps '''
    return time.mktime(time.gmtime())


def get_response(url, ccy, params=None, body=None, header=None):
    ''' Method for executing API requests '''
    guard(url, ccy)
    if ccy:
        url = url % ccy
    if params:
        url = "%s%s" % (url, params)
    try:
        if body:
            data = json.loads(body)
            response = requests.post(url, json=data)
        else:
            response = requests.get(url,headers=header)
        response.raise_for_status()
        return response.json()
    except Exception as exc:
        print("Exception during request %s : %s " % (url, exc))
        print('-' * 60)
        traceback.print_exc(file=sys.stdout)
        print('-' * 60)


def get_orders(data, max_qty, bids_tag, asks_tag, price_tag=0, qty_tag=1):
    ''' Method for extracting orders '''
    orders = {}
    bids = {}
    asks = {}
    buymax = 0
    sellmax = 0
    for level in data[bids_tag]:
        if buymax > max_qty:
            continue
        else:
            bids[apply_format_level(level[price_tag])] = "{:.8f}".format(float(level[qty_tag]))
        buymax = buymax + float(level[qty_tag])

    for level in data[asks_tag]:
        if sellmax > max_qty:
            continue
        else:
            asks[apply_format_level(level[price_tag])] = "{:.8f}".format(float(level[qty_tag]))
        sellmax = sellmax + float(level[qty_tag])
    orders["source"] = "ITBIT"
    orders["bids"] = bids
    orders["asks"] = asks
    orders["timestamp"] = str(int(time.time()))
    return orders


def guard(url, ccy):
    ''' Method for checking inputs '''
    if ccy:
        if '%' not in url:
            raise ValueError("URL %s does not have a % for insertin supplied ccy " % (url, ccy))
    else:
        if '%' in url:
            raise ValueError("URL %s should have a currency value supplied" % url)
