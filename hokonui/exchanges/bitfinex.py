''' Module for testing Bitfinex API '''
# pylint: disable=duplicate-code, line-too-long

import time
from hokonui.exchanges.base import Exchange as Base
from hokonui.models.ticker import Ticker
from hokonui.utils.helpers import apply_format
from hokonui.utils.helpers import apply_format_level


class Bitfinex(Base):
    ''' class for testing Bitfinex public information API  '''

    TICKER_URL = 'https://api.bitfinex.com/v1/pubticker/btc%s'
    ORDER_BOOK_URL = 'https://api.bitfinex.com/v1/book/btc%s'
    NAME = 'Bitfinex'

    @classmethod
    def _current_price_extractor(cls, data):
        ''' Method for extracting current price '''
        return apply_format(data.get('last_price'))

    @classmethod
    def _current_bid_extractor(cls, data):
        ''' Method for extracting bid price '''
        return apply_format(data.get('bid'))

    @classmethod
    def _current_ask_extractor(cls, data):
        ''' Method for extracting ask price '''
        return apply_format(data.get('ask'))

    @classmethod
    def _current_ticker_extractor(cls, data):
        ''' Method for extracting ticker '''
        bid = apply_format(data.get('bid'))
        ask = apply_format(data.get('ask'))
        return Ticker(cls.CCY_DEFAULT, bid, ask).toJSON()

    @classmethod
    def _current_orders_extractor(cls, data, max_qty=3):
        ''' Method for extracting orders '''
        orders = {}
        bids = {}
        asks = {}
        buymax = 0
        sellmax = 0
        for level in data["bids"]:
            if buymax > max_qty:
                continue
            else:
                bids[apply_format_level(level["price"])] = "{:.8f}".format(
                    float(level["amount"]))
            buymax = buymax + float(level["amount"])

        for level in data["asks"]:
            if sellmax > max_qty:
                continue
            else:
                asks[apply_format_level(level["price"])] = "{:.8f}".format(
                    float(level["amount"]))
            sellmax = sellmax + float(level["amount"])

        orders["source"] = "Bitfinex"
        orders["bids"] = bids
        orders["asks"] = asks
        orders["timestamp"] = str(int(time.time()))
        return orders
