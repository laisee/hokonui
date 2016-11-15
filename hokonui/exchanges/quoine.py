import time
from hokonui.exchanges.base import Exchange
from hokonui.models.ticker import Ticker
from hokonui.utils.helpers import apply_format, apply_format_level


class Quoine(Exchange):

    TICKER_URL = 'https://api.quoine.com/products/code/CASH/BTC%s'
    ORDER_BOOK_URL = 'https://api.quoine.com/products/%s/price_levels'
    NAME = "Quoine"

    @classmethod
    def _current_price_extractor(cls, data):
        return apply_format(data.get('last_traded_price'))

    @classmethod
    def _current_bid_extractor(cls, data):
        return apply_format(data.get('market_bid'))

    @classmethod
    def _current_ask_extractor(cls, data):
        return apply_format(data.get('market_ask'))

    @classmethod
    def _current_ticker_extractor(cls, data):
        return Ticker(cls.CCY_DEFAULT, apply_format(data.get('market_bid')), apply_format(data.get('market_ask'))).toJSON()

    @classmethod
    def _current_orders_extractor(cls, data, max_qty=3):

        orders = {}
        bids = {}
        asks = {}
        buyMax = 0
        sellMax = 0
        print data
        for level in data["buy_price_levels"]:
            if buyMax > max_qty:
                pass
            else:
                asks[apply_format_level(level[0])] = "{:.8f}".format(float(level[1]))
            buyMax = buyMax + float(level[1])

        for level in data["sell_price_levels"]:
            if sellMax > max_qty:
                pass
            else:
                bids[apply_format_level(level[0])] = "{:.8f}".format(float(level[1]))
            sellMax = sellMax + float(level[1])

        orders["source"] = cls.NAME
        orders["bids"] = bids
        orders["asks"] = asks
        orders["timestamp"] = str(int(time.time()))
        return orders
