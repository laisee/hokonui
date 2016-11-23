''' Module for testing BTCC API '''
# pylint: disable=duplicate-code, line-too-long
import time
from hokonui.exchanges.base import Exchange
from hokonui.models.ticker import Ticker
from hokonui.utils.helpers import apply_format
from hokonui.utils.helpers import apply_format_level


class BtcXIndia(Exchange):
    ''' Class for testing BTCC API '''

    TICKER_URL = 'https://api.btcxindia.com/ticker'
    ORDER_BOOK_URL = 'https://www.okcoin.com/api/v1/depth.do?symbol=btc_usd&size=10'
    NAME = "BtcXIndia"

    @classmethod
    def _current_price_extractor(cls, data):
        return apply_format(data['last_traded_price'])

    @classmethod
    def _current_bid_extractor(cls, data):
        return apply_format(data['bid'])

    @classmethod
    def _current_ask_extractor(cls, data):
        return apply_format(data['ask'])

    @classmethod
    def _current_ticker_extractor(cls, data):
        return Ticker(cls.CCY_DEFAULT, apply_format(data['bid']), apply_format(data['ask'])).toJSON()

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
                bids[apply_format_level(level[0])] = "{:.8f}".format(float(level[1]))
            buymax = buymax + float(level[1])

        for level in data["asks"]:
            if sellmax > max_qty:
                pass
            else:
                asks[apply_format_level(level[0])] = "{:.8f}".format(float(level[1]))
            sellmax = sellmax + float(level[1])

        orders["source"] = "BtcXIndia"
        orders["bids"] = bids
        orders["asks"] = asks
        orders["timestamp"] = str(int(time.time()))
        return orders
