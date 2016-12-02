''' Module for testing Space BTC API '''
# pylint: disable=duplicate-code, line-too-long
import time
from hokonui.exchanges.base import Exchange
from hokonui.models.ticker import Ticker
from hokonui.utils.helpers import apply_format
from hokonui.utils.helpers import apply_format_level


class SpaceBTC(Exchange):
    ''' Class for testing Space BTC API '''

    TICKER_URL = 'https://tapi.spacebtc.com/ticker/%s'
    ORDER_BOOK_URL = 'https://tapi.spacebtc.com/depth/%s'
    NAME = "SpaceBTC"

    @classmethod
    def _current_price_extractor(cls, data):
        return apply_format(data["result"]["last"])

    @classmethod
    def _current_bid_extractor(cls, data):
        return apply_format(data["result"]["bid"])

    @classmethod
    def _current_ask_extractor(cls, data):
        return apply_format(data["result"]["ask"])

    @classmethod
    def _current_ticker_extractor(cls, data):
        return Ticker(cls.CCY_DEFAULT, apply_format(data["result"]['bid']), apply_format(data["result"]['bid'])).toJSON()

    @classmethod
    def _current_orders_extractor(cls, data, max_qty=3):
        orders = {}
        bids = {}
        asks = {}
        buymax = 0
        sellmax = 0
        for level in data["result"]["bids"]:
            if buymax > max_qty:
                pass
            else:
                bids[apply_format_level(level[0])] = "{:.8f}".format(float(level[1]))
            buymax = buymax + float(level[1])

        for level in data["result"]["asks"]:
            if sellmax > max_qty:
                pass
            else:
                asks[apply_format_level(level[0])] = "{:.8f}".format(float(level[1]))
            sellmax = sellmax + float(level[1])

        orders["source"] = "SpaceBTC"
        orders["bids"] = bids
        orders["asks"] = asks
        orders["timestamp"] = str(int(time.time()))
        return orders
