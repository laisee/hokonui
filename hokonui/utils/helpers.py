''' Module containing helper methods '''
# pylint: disable=duplicate-code, line-too-long

import json
import sys
import traceback
import time
from datetime import datetime
from decimal import Decimal
import requests


def docstring_parameter(*sub):
    ''' Method for managing params '''

    def dec(obj):
        obj.__doc__ = obj.__doc__.format(*sub)
        return obj

    return dec


def apply_format(value, precision='.5f'):
    ''' Method for applying formats '''

    return format(Decimal(value), precision)


def apply_format_level(value, precision='.2f'):
    ''' Method for applying format levels '''

    return format(Decimal(value), precision)


def get_datetime():
    ''' Method for generating datetime value '''

    return datetime.now().strftime('%Y-%m-%d %h:%m:%s')


def get_timestamp():
    ''' Method for calculating UTC timestamps '''

    return time.mktime(time.gmtime())


def get_response(url, ccy, params=None, body=None, header=None):
    ''' Method for executing API requests '''

    guard(url, ccy)
    if ccy:
        url = url % ccy

    if params:
        url = "%s%s" % (url, params)

    rsp = None

    try:
        if body:
            data = json.loads(body)
            response = requests.post(url, json=data)
        else:
            response = requests.get(url, headers=header)
        response.raise_for_status()
        rsp = response.json()
    except requests.ConnectionError as cex:
        print("Exception during request %s : %s " % (url, cex))
        print('-' * 60)
        traceback.print_exc(file=sys.stdout)
        print('-' * 60)
    return rsp


def guard(url, ccy):
    ''' Method for checking inputs '''

    print("URL ", url)
    if ccy:
        if '%' not in url:
            raise ValueError("URL %s does not have place for ccy %s " % (url, ccy))
    else:
        if '%' in url:
            raise ValueError("URL %s should have a currency value supplied" % url)
