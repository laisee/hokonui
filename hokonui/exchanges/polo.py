
''' Module for testing Poloniex API '''
# pylint: disable=duplicate-code, line-too-long
import time
from hokonui.exchanges.base import Exchange
from hokonui.models.ticker import Ticker
from hokonui.utils.helpers import apply_format, apply_format_level


class Poloniex(Exchange):
    '''
    Class for Poloniex API

    '''

    TICKER_URL = 'https://poloniex.com/public?command=returnTicker'
    ORDER_BOOK_URL = 'https://poloniex.com/public?command=returnOrderBook&currencyPair=%s&depth=10'
    CCY_DEFAULT = "BTC_XEM"
    NAME = "Poloniex"

    @classmethod
    def _current_price_extractor(cls, data):
        return apply_format(str(data[cls.CCY_DEFAULT]["last"]))

    @classmethod
    def _current_bid_extractor(cls, data):
        return apply_format(str(data[cls.CCY_DEFAULT]["highestBid"]))

    @classmethod
    def _current_ask_extractor(cls, data):
        return apply_format(str(data[cls.CCY_DEFAULT]["lowestAsk"]))

    @classmethod
    def _current_ticker_extractor(cls, data):
        ask = apply_format(str(data[cls.CCY_DEFAULT]["last"]))
        bid = apply_format(str(data[cls.CCY_DEFAULT]["last"]))
        return Ticker(cls.CCY_DEFAULT, bid, ask).toJSON()

    @classmethod
    def _current_orders_extractor(cls, data, max_qty=3):
        orders = {}
        asks = {}
        bids = {}

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
