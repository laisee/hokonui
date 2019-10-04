''' Module for testing Cryptofacility API '''
# pylint: disable=duplicate-code, line-too-long
import time
from hokonui.exchanges.base import Exchange as Base
from hokonui.models.ticker import Ticker
from hokonui.utils.helpers import apply_format


class CryptoFacility(Base):
    ''' Class for testing Cryptofac API '''

    TICKER_URL = 'https://www.cryptofacilities.com/derivatives/api/v3/tickers/'
    ORDER_BOOK_URL = 'https://www.cryptofacilities.com/derivatives/api/v3/orderbook?symbol=%s'
    NAME = 'CryptoFacility'

    @classmethod
    def _current_price_extractor(cls, data):
        price = data["tickers"][5]["last"]
        return apply_format(price)

    @classmethod
    def _current_bid_extractor(cls, data):
        bid = data["tickers"][5]["bid"]
        return apply_format(bid)

    @classmethod
    def _current_ask_extractor(cls, data):
        ask = data["tickers"][5]["ask"]
        return apply_format(ask)

    @classmethod
    def _current_ticker_extractor(cls, data):
        ask = data["tickers"][5]["ask"]
        bid = data["tickers"][5]["bid"]
        return Ticker(cls.CCY_DEFAULT, apply_format(bid),
                      apply_format(ask)).toJSON()

    @classmethod
    def _current_orders_extractor(cls, data, max_qty=3):
        orders = {}
        bids = {}
        asks = {}
        # buymax = 0
        # sellmax = 0
        # for level in data["orderBook"]["bids"]:
        #    if buymax > max_qty:
        #        continue
        #    else:
        #        bids[apply_format_level(level[0])] = "{:.8f}".format(float(level[1]))
        #    buymax = buymax + float(level[1])

        # for level in data["orderBook"]["asks"]:
        #    if sellmax > max_qty:
        #        continue
        #    else:
        #        asks[apply_format_level(level[0])] = "{:.8f}".format(float(level[1]))
        #    sellmax = sellmax + float(level[1])

        orders["source"] = cls.NAME
        orders["bids"] = bids
        orders["asks"] = asks
        orders["timestamp"] = str(int(time.time()))
        return orders
