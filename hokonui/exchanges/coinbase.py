''' Module for testing Coinbase API '''
# pylint: disable=duplicate-code, line-too-long
import time
from hokonui.exchanges.base import Exchange
from hokonui.models.ticker import Ticker
from hokonui.utils.helpers import apply_format, apply_format_level


class CoinBase(Exchange):
    ''' Class for testing Coinbase API '''

    TICKER_URL = "https://api.coinbase.com/v2/prices/BTC-%s/spot"
    PRICE_URL  = "https://api.coinbase.com/v2/prices/BTC-%s/spot"
    BID_URL = "https://api.coinbase.com/v2/prices/BTC-%s/buy"
    ASK_URL = "https://api.coinbase.com/v2/prices/BTC-%s/sell"
    HEADER = { "CB-VERSION": "2016-02-18" }
    ORDER_BOOK_URL = 'https://api.gdax.com/products/BTC-%s/book?level=2'
    NAME = 'Coinbase'

    @classmethod
    def _current_price_extractor(cls, data):
        return apply_format(data["data"]["amount"])

    @classmethod
    def _current_bid_extractor(cls, data):
        return apply_format(data["data"]["amount"])

    @classmethod
    def _current_ask_extractor(cls, data):
        return apply_format(data["data"]["amount"])

    @classmethod
    def _current_ticker_extractor(cls, data):
        bid =  apply_format(data["data"]["amount"])
        ask =  apply_format(data["data"]["amount"])
        return Ticker(cls.CCY_DEFAULT, bid, ask).toJSON()

    @classmethod
    def _current_orders_extractor(cls, data, max_qty=3):
        orders = {}
        bids = {}
        asks = {}
        buymax = 0
        sellmax = 0
        for level in data["bids"]:
            if buymax > max_qty:
                pass
            else:
                asks[apply_format_level(level[0])] = "{:.8f}".format(float(level[1]))
            buymax = buymax + float(level[1])

        for level in data["asks"]:
            if sellmax > max_qty:
                pass
            else:
                bids[apply_format_level(level[0])] = "{:.8f}".format(float(level[1]))
            sellmax = sellmax + float(level[1])

        orders["source"] = cls.NAME
        orders["bids"] = bids
        orders["asks"] = asks
        orders["timestamp"] = str(int(time.time()))
        return orders
