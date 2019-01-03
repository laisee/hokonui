''' Module for Exchange base class '''
# pylint: disable=duplicate-code, line-too-long
from hokonui.utils.helpers import get_response

class Exchange(object):
    ''' Class Exchange base class for all exchanges '''

    TICKER_URL = None
    ORDER_BOOK_URL = None
    VOLUME_URL = None
    PRICE_URL = None
    NAME = 'BitThumb'
    CCY_DEFAULT = 'USD'

    @classmethod
    def _current_price_extractor(cls, data):
        ''' Method for extracting current price '''
        raise NotImplementedError

    @classmethod
    def _current_bid_extractor(cls, data):
        ''' Method for extracting bid price '''
        raise NotImplementedError

    @classmethod
    def _current_ask_extractor(cls, data):
        ''' Method for extracting ask price '''
        raise NotImplementedError

    @classmethod
    def _current_orders_extractor(cls, data, max_qty=100):
        ''' Method for extracting orders '''
        raise NotImplementedError

    @classmethod
    def _current_ticker_extractor(cls, data):
        ''' Method for extracting ticker '''
        raise NotImplementedError

    @classmethod
    def get_current_price(cls, ccy=None, params=None, body=None, header=None):
        ''' Method for retrieving last price '''
        url = cls.PRICE_URL if hasattr(cls, 'PRICE_URL') and cls.PRICE_URL is not None else cls.TICKER_URL
        print(url)
        data = get_response(url, ccy, params, body, header)
        print(data)
        return cls._current_price_extractor(data)

    @classmethod
    def get_current_bid(cls, ccy=None, params=None, body=None, header=None):
        ''' Method for retrieving current bid price '''
        url = cls.BID_URL if hasattr(cls, 'BID_URL') and cls.BID_URL is not None else cls.TICKER_URL
        data = get_response(url, ccy, params, body, header)
        return cls._current_bid_extractor(data)

    @classmethod
    def get_current_ask(cls, ccy=None, params=None, body=None, header=None):
        ''' Method for retrieving current ask price '''
        url = cls.ASK_URL if hasattr(cls, 'ASK_URL') and cls.ASK_URL is not None else cls.TICKER_URL
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
