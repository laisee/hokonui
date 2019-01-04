''' Module for testing Huobi API '''
# pylint: disable=duplicate-code, line-too-long

import time
from hokonui.exchanges.base import Exchange as Base
from hokonui.models.ticker import Ticker
from hokonui.utils.helpers import apply_format, apply_format_level


class Huobi(Base):
    ''' Class for testing Huobi API '''

    TICKER_URL = 'http://api.huobi.com/staticmarket/ticker_btc_json.js'
    ORDER_BOOK_URL = 'http://api.huobi.com/staticmarket/detail_btc_json.js'
    NAME = 'Huobi'

    @classmethod
    def _current_price_extractor(cls, data):
        ''' Method for extracting current price '''
        return apply_format(data.get('ticker', {}).get('last'))

    @classmethod
    def _current_bid_extractor(cls, data):
        ''' Method for extracting current bid price '''
        return apply_format(data.get('ticker', {}).get('buy'))

    @classmethod
    def _current_ask_extractor(cls, data):
        ''' Method for extracting current ask price '''
        return apply_format(data.get('ticker', {}).get('sell'))

    @classmethod
    def _current_ticker_extractor(cls, data):
        ''' Method for extracting current ticker '''
        return Ticker(cls.CCY_DEFAULT, apply_format(data.get('ticker', {}).get('buy')), apply_format(data.get('ticker', {}).get('sell'))).toJSON()

    @classmethod
    def _current_orders_extractor(cls, data, max_qty=100):
        ''' Method for extracting current orders '''
        orders = {}
        bids = {}
        asks = {}
        buymax = 0
        sellmax = 0
        for level in data["top_buy"]:
            if buymax > max_qty:
                continue
            else:
                bids[apply_format_level(level["price"])] = "{:.8f}".format(float(level["amount"]))
            buymax = buymax + float(level["amount"])

        for level in data["top_sell"]:
            if sellmax > max_qty:
                continue
            else:
                asks[apply_format_level(level["price"])] = "{:.8f}".format(float(level["amount"]))
            sellmax = sellmax + float(level["amount"])
        orders["source"] = "Huobi"
        orders["bids"] = bids
        orders["asks"] = asks
        orders["timestamp"] = str(int(time.time()))
        return orders
