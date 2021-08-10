''' Module for testing OkCoin API '''
# pylint: disable=fixme, line-too-long

import time
from hokonui.exchanges.base import Exchange as Base
from hokonui.models.ticker import Ticker
from hokonui.utils.helpers import apply_format
from hokonui.utils.helpers import apply_format_level


class OKCoin(Base):
    ''' Class for testing OkCoin API '''

    TICKER_URL = "https://www.okcoin.com/api/spot/v3/instruments/BTC-USDT/ticker"
    ORDER_BOOK_URL = "https://www.okcoin.com/api/spot/v3/instruments/BTC-USDT/book?size=5&depth=0.2"

    @classmethod
    def _current_price_extractor(cls, data):
        return apply_format(data['last'])

    @classmethod
    def _current_bid_extractor(cls, data):
        return apply_format(data["bid"])

    @classmethod
    def _current_ask_extractor(cls, data):
        return apply_format(data["ask"])

    @classmethod
    def _current_ticker_extractor(cls, data):
        bid = apply_format(data["bid"])
        ask = apply_format(data["ask"])
        return Ticker(cls.CCY_DEFAULT, bid, ask).to_json()

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
                bids[apply_format_level(level[0])] = "{:.8f}".format(
                    float(level[1]))
            buymax = buymax + float(level[1])

        for level in data["asks"]:
            if sellmax > max_qty:
                pass
            else:
                asks[apply_format_level(level[0])] = "{:.8f}".format(
                    float(level[1]))
            sellmax = sellmax + float(level[1])

        orders["source"] = "OKCoin"
        orders["bids"] = bids
        orders["asks"] = asks
        orders["timestamp"] = str(int(time.time()))
        return orders
