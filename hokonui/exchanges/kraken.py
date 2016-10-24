import time
import json
from hokonui.exchanges.base import Exchange
from hokonui.models.ticker import Ticker
from hokonui.utils.helpers import apply_format, apply_format_level

class Kraken(Exchange):

    TICKER_URL = 'https://api.kraken.com/0/public/Ticker'
    ORDER_BOOK_URL = 'https://api.kraken.com/0/public/Depth'
    NAME = 'Kraken'

    @classmethod
    def _current_price_extractor(cls, data):
        print "Data : ",data
        pair = data["result"].keys()[0]
        last = data["result"][pair]["c"][0]
        return apply_format(last)

    @classmethod
    def _current_bid_extractor(cls, data):
        pair = data["result"].keys()[0]
        bid = data["result"][pair]["b"][0]
        return apply_format(bid)

    @classmethod
    def _current_ask_extractor(cls, data):
        pair = data["result"].keys()[0]
        ask = data["result"][pair]["a"][0]
        return apply_format(ask)

    @classmethod
    def _current_ticker_extractor(cls, data):
        pair = data["result"].keys()[0]
        ask = data["result"][pair]["a"][0]
        bid = data["result"][pair]["b"][0]
        return Ticker(pair,apply_format(bid),apply_format(ask)).toJSON()

    @classmethod
    def _current_orders_extractor(cls,data,max_qty=100.0):
        orders = {}
        ask = ""
        bid = ""
        bids = {}
        asks = {}
        buyMax = 0.0
        sellMax = 0.0
        pair = data["result"].keys()[0]
        print "PAIR ", pair
        print "MAX Qty :", max_qty
        for level in data["result"][pair]["bids"]:
            print level
            if buyMax > max_qty:
                pass
            else:
                print level[0]
                asks[apply_format_level(level[0])] = "{:.8f}".format(float(level[1]))
                buyMax = buyMax + float(level[1])
                print buyMax, " < ", max_qty
 
        for level in data["result"][pair]["asks"]:
            print level
            if sellMax > max_qty:
                pass
            else:
                print level[0]
                bids[apply_format_level(level[0])] = "{:.8f}".format(float(level[1]))
                sellMax = sellMax + float(level[1])
                print sellMax, " < ", max_qty
        orders["source"] = "Kraken"
        orders["bids"] = bids
        orders["asks"] = asks
        orders["timestamp"] = str(int(time.time()))
        return orders
