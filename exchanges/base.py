from decimal import Decimal
from helpers import get_response, get_datetime


class Exchange(object):

    TICKER_URL = None
    ORDER_BOOK_URL = None
    NAME = 'Base'

    @classmethod
    def _current_price_extractor(cls, data):
        raise NotImplementedError

    @classmethod
    def _current_bid_extractor(cls, data):
        raise NotImplementedError

    @classmethod
    def _current_ask_extractor(cls, data):
        raise NotImplementedError

    @classmethod
    def _current_ask_orders_extractor(cls, data):
        raise NotImplementedError

    @classmethod
    def _current_orders_extractor(cls, data):
        raise NotImplementedError

    @classmethod
    def get_current_price(cls,ccy=None):
        body = cls.BODY if hasattr(cls, 'BODY') else None
        data = get_response(cls.TICKER_URL,ccy,body)
        return cls._current_price_extractor(data)

    @classmethod
    def get_current_bid(cls,ccy=None):
        body = cls.BODY if hasattr(cls, 'BODY') else None
        data = get_response(cls.TICKER_URL,ccy,body)
        return cls._current_bid_extractor(data)

    @classmethod
    def get_current_ask(cls,ccy=None):
        body = cls.BODY if hasattr(cls, 'BODY') else None
        data = get_response(cls.TICKER_URL,ccy,body)
        return cls._current_ask_extractor(data)

    @classmethod
    def get_current_orders(cls,ccy=None,max_qty=5):
        body = cls.BODY if hasattr(cls, 'BODY') else None
        data = get_response(cls.ORDER_BOOK_URL,ccy,body)
        return cls._current_orders_extractor(data,max_qty)
