''' Module for Exchange base class '''
# pylint: disable=duplicate-code, line-too-long

import time
from hokonui.models.ticker import Ticker
from hokonui.utils.helpers import apply_format_level


class Mock():
    ''' Class Mock exchanges '''

    TICKER_URL = None
    ORDER_BOOK_URL = None
    VOLUME_URL = None
    PRICE_URL = None
    NAME = 'Mock'
    CCY_DEFAULT = 'USD'
    MOCK_PRICE = 1.2345
    MOCK_ASK_QTY = 12.88
    MOCK_BID_QTY = 12.99

    @classmethod
    def _current_price_extractor(cls, data):
        ''' Method for extracting current price '''

        assert cls is not None
        return data["price"]

    @classmethod
    def _current_bid_extractor(cls, data):
        ''' Method for extracting bid price '''

        assert cls is not None
        return data["bid"]

    @classmethod
    def _current_ask_extractor(cls, data):
        ''' Method for extracting ask price '''

        assert cls is not None
        return data["ask"]

    @classmethod
    def _current_orders_extractor(cls, data, max_qty=100):
        ''' Method for extracting orders '''

        assert cls is not None
        orders = {}
        bids = {}
        asks = {}
        buymax = 0
        sellmax = 0
        for level in data["bids"]:
            if buymax > max_qty:
                pass
            else:
                asks[apply_format_level(level["price"],
                                        '.2f')] = "{:.8f}".format(
                                            float(level["quantity"]))
            buymax = buymax + float(level["quantity"])

        for level in data["asks"]:
            if sellmax > max_qty:
                pass
            else:
                bids[apply_format_level(level["price"],
                                        '.2f')] = "{:.8f}".format(
                                            float(level["quantity"]))
            sellmax = sellmax + float(level["quantity"])

        orders["source"] = cls.NAME
        orders["bids"] = bids
        orders["asks"] = asks
        orders["timestamp"] = str(int(time.time()))
        print(orders)
        return orders

    @classmethod
    def _current_ticker_extractor(cls, data):
        ''' Method for extracting ticker '''

        assert cls is not None
        assert data is not None
        return Ticker(cls.CCY_DEFAULT, data["ask"], data["bid"]).to_json()

    @classmethod
    def get_current_price(cls, ccy=None, params=None, body=None, header=None):
        ''' Method for retrieving last price '''

        assert cls is not None
        if ccy is not None:
            print(ccy)
        if params is not None:
            print(params)
        if body is not None:
            print(body)
        if header is not None:
            print(header)
        data = {"price": cls.MOCK_PRICE}
        return cls._current_price_extractor(data)

    @classmethod
    def get_current_bid(cls, ccy=None, params=None, body=None, header=None):
        ''' Method for retrieving current bid price '''
        data = {"bid": cls.MOCK_PRICE}
        if ccy is not None:
            print(ccy)
        if params is not None:
            print(params)
        if body is not None:
            print(body)
        if header is not None:
            print(header)
        return cls._current_bid_extractor(data)

    @classmethod
    def get_current_ask(cls, ccy=None, params=None, body=None, header=None):
        ''' Method for retrieving current ask price '''
        data = {"ask": cls.MOCK_PRICE}
        if ccy is not None:
            print(ccy)
        if params is not None:
            print(params)
        if body is not None:
            print(body)
        if header is not None:
            print(header)
        return cls._current_ask_extractor(data)

    @classmethod
    def get_current_ticker(cls, ccy=None, params=None, body=None, header=None):
        ''' Method for retrieving current ticker '''

        data = {"ask": cls.MOCK_PRICE, "bid": cls.MOCK_PRICE}
        if ccy is not None:
            print(ccy)
        if params is not None:
            print(params)
        if body is not None:
            print(body)
        if header is not None:
            print(header)
        return cls._current_ticker_extractor(data)

    @classmethod
    def get_current_orders(cls, ccy=None, params=None, body=None, max_qty=5):
        ''' Method for retrieving current orders '''
        data = {
            "asks": [{
                "price": cls.MOCK_PRICE,
                "quantity": "12.99"
            }],
            "bids": [{
                "price": cls.MOCK_PRICE,
                "quantity": "12.88"
            }]
        }
        if ccy is not None:
            print(ccy)
        if params is not None:
            print(params)
        if body is not None:
            print(body)
        if max_qty is not None:
            print(max_qty)
        return cls._current_orders_extractor(data, max_qty)
