''' Module for testing Huobi API '''
# pylint: disable=duplicate-code, line-too-long

import time
from hokonui.exchanges.base import Exchange as Base
from hokonui.models.ticker import Ticker
from hokonui.utils.helpers import apply_format, apply_format_level


class Huobi(Base):
    ''' Class for testing Huobi API '''

    NAME = 'Huobi'
    CCY_DEFAULT = "BTCUSDT"
    TICKER_URL = 'https://api.huobi.pro/market/detail/merged?symbol=btcusdt'
    ORDER_BOOK_URL = 'https://api.huobi.pro/market/depth?symbol=btcusdt&type=step1'

    @classmethod
    def _current_price_extractor(cls, data):
        ''' Method for extracting current price '''
        return apply_format(data["tick"]['ask'][0] - data["tick"]['bid'][0])

    @classmethod
    def _current_bid_extractor(cls, data):
        ''' Method for extracting current bid price '''
        return apply_format(data["tick"]['bid'][0])

    @classmethod
    def _current_ask_extractor(cls, data):
        ''' Method for extracting current ask price '''
        return apply_format(data["tick"]['ask'][0])

    @classmethod
    def _current_ticker_extractor(cls, data):
        ''' Method for extracting current ticker '''
        return Ticker(cls.CCY_DEFAULT, apply_format(data["tick"]['bid'][0]), apply_format(data["tick"]['ask'][0])).to_json()

    @classmethod
    def _current_orders_extractor(cls, data, max_qty=100):
        ''' Method for extracting current orders '''
        orders = {}
        bids = {}
        asks = {}
        buymax = 0
        sellmax = 0
        for level in data["tick"]["bids"]:
            if buymax > max_qty:
                continue
            else:
                bids[apply_format_level(level[0])] = "{:.8f}".format(
                    float(level[1]))
            buymax = buymax + float(level[1])

        for level in data["tick"]["asks"]:
            if sellmax > max_qty:
                continue
            else:
                asks[apply_format_level(level[0])] = "{:.8f}".format(
                    float(level[1]))
            sellmax = sellmax + float(level[1])
        orders["source"] = "Huobi"
        orders["bids"] = bids
        orders["asks"] = asks
        orders["timestamp"] = str(int(time.time()))
        return orders
