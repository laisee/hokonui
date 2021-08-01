''' Module for Exchange base class '''
# pylint: disable=duplicate-code, line-too-long

import time
from hokonui.exchanges.base import Exchange as Base
from hokonui.models.ticker import Ticker
from hokonui.utils.helpers import apply_format
from hokonui.utils.helpers import apply_format_level
from hokonui.utils.helpers import get_response


class Kucoin(Base):
    ''' Class Exchange base class for all exchanges '''


    ASK_URL = None
    BID_URL = None
    PRICE_URL = None
    TICKER_URL     = "https://api.kucoin.com/api/v1/market/orderbook/level1?symbol=BTC-USDT"
    ORDER_BOOK_URL = "https://api.kucoin.com/api/v1/market/orderbook/level2_20?symbol=BTC-USDT"
    NAME = 'Kucoin'
    CCY_DEFAULT = 'USDT'

    @classmethod
    def _current_price_extractor(cls, data):
        ''' Method for extracting current price '''
        return apply_format(data["data"].get('price'))

    @classmethod
    def _current_bid_extractor(cls, data):
        ''' Method for extracting bid price '''
        return apply_format(data["data"].get('bestBid'))

    @classmethod
    def _current_ask_extractor(cls, data):
        ''' Method for extracting ask price '''
        return apply_format(data["data"].get('bestAsk'))

    @classmethod
    def _current_orders_extractor(cls, data, max_qty=100):
        ''' Method for extracting orders '''
        print("DATA ",data) 
        orders = {}
        bids = {}
        asks = {}
        buymax = 0
        sellmax = 0
        for level in data["data"]["bids"]:
            if buymax > max_qty:
                pass
            else:
                asks[apply_format_level(level[0])] = "{:.8f}".format(
                    float(level[1]))
            buymax = buymax + float(level[1])

        for level in data["data"]["asks"]:
            if sellmax > max_qty:
                pass
            else:
                bids[apply_format_level(level[0])] = "{:.8f}".format(
                    float(level[1]))
            sellmax = sellmax + float(level[1])

        orders["source"] = cls.NAME
        orders["bids"] = bids
        orders["asks"] = asks
        orders["timestamp"] = str(int(time.time()))
        return orders

    @classmethod
    def _current_ticker_extractor(cls, data):
        ''' Method for extracting ticker '''
        bid = apply_format(data["data"].get('bestBid'))
        ask = apply_format(data["data"].get('bestAsk'))
        return Ticker(cls.CCY_DEFAULT, bid, ask).toJSON()

    @classmethod
    def get_current_price(cls, ccy=None, params=None, body=None, header=None):
        ''' Method for retrieving last price '''
        url = cls.PRICE_URL if hasattr(
            cls, 'PRICE_URL') and cls.PRICE_URL is not None else cls.TICKER_URL
        data = get_response(url, ccy, params, body, header)
        return cls._current_price_extractor(data)

    @classmethod
    def get_current_bid(cls, ccy=None, params=None, body=None, header=None):
        ''' Method for retrieving current bid price '''
        url = cls.BID_URL if hasattr(
            cls, 'BID_URL') and cls.BID_URL is not None else cls.TICKER_URL
        data = get_response(url, ccy, params, body, header)
        return cls._current_bid_extractor(data)

    @classmethod
    def get_current_ask(cls, ccy=None, params=None, body=None, header=None):
        ''' Method for retrieving current ask price '''
        url = cls.ASK_URL if hasattr(
            cls, 'ASK_URL') and cls.ASK_URL is not None else cls.TICKER_URL
        data = get_response(url, ccy, params, body, header)
        return cls._current_ask_extractor(data)

    @classmethod
    def get_current_ticker(cls, ccy=None, params=None, body=None, header=None):
        ''' Method for retrieving current ticker '''
        data = get_response(cls.TICKER_URL, ccy, params, body, header)
        return cls._current_ticker_extractor(data)

    @classmethod
    def get_current_orders(cls, ccy=None, params=None, body=None, max_qty=5):
        ''' Method for retrieving current orders '''

        data = get_response(cls.ORDER_BOOK_URL, ccy, params, body)
        return cls._current_orders_extractor(data, max_qty)
