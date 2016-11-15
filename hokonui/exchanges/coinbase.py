import time
from hokonui.exchanges.base import Exchange
from hokonui.models.ticker import Ticker
from hokonui.utils.helpers import apply_format, apply_format_level


class CoinBase(Exchange):

    TICKER_URL = 'https://api.exchange.coinbase.com/products/BTC-%s/'
    ORDER_BOOK_URL = 'https://api.exchange.coinbase.com/products/BTC-%s/book?level=2'
    NAME = 'CoinBase'

    @classmethod
    def _current_price_extractor(cls, data):
        print data
        return apply_format(data.get('price'))

    @classmethod
    def _current_bid_extractor(cls, data):
        return apply_format(data["bids"][0][0])

    @classmethod
    def _current_ask_extractor(cls, data):
        return apply_format(data["asks"][0][0])

    @classmethod
    def _current_ticker_extractor(cls, data):
        return Ticker(cls.CCY_DEFAULT, apply_format(data["bids"][0][0]), apply_format(data["asks"][0][0])).toJSON()

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
