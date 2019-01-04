
''' Module for testing Zaif API '''
# pylint: disable=duplicate-code, line-too-long

import time
from hokonui.exchanges.base import Exchange as Base
from hokonui.models.ticker import Ticker
from hokonui.utils.helpers import apply_format, apply_format_level


class Nem(Base):
    '''
    Class for NEM API

    '''

    TICKER_URL = 'https://api.coinmarketcap.com/v1/ticker/nem'
    ORDER_BOOK_URL = 'https://api.coinmarketcap.com/v1/ticker/nem'
    CCY_DEFAULT = "XEM_USD"
    NAME = "NEM"

    @classmethod
    def _current_price_extractor(cls, data):
        print(data)
        return apply_format(str(data[0]['price_usd']))

    @classmethod
    def _current_bid_extractor(cls, data):
        return apply_format(str(data[0]['price_usd']))

    @classmethod
    def _current_ask_extractor(cls, data):
        return apply_format(str(data[0]['price_usd']))

    @classmethod
    def _current_ticker_extractor(cls, data):
        ask =  apply_format(data[0]['price_usd'])
        bid =  apply_format(data[0]['price_usd'])
        return Ticker(cls.CCY_DEFAULT, bid, ask).toJSON()

    @classmethod
    def _current_orders_extractor(cls, data, max_qty=3):
        orders = {}
        asks = {}
        bids = {}
        orders["source"] = cls.NAME
        orders["bids"] = bids
        orders["asks"] = asks
        orders["timestamp"] = str(int(time.time()))
        return orders
