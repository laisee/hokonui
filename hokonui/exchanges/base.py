""" Module for Exchange base class """

# pylint: disable=duplicate-code, line-too-long

from hokonui.utils.helpers import get_response


class Exchange:
    """Class Exchange base class for all exchanges"""

    ASK_URL: str = None
    BID_URL: str = None
    PRICE_URL: str = None
    TICKER_URL: str = None
    ORDER_BOOK_URL: str = None
    VOLUME_URL: str = None
    PRICE_URL: str = None
    NAME: str = "Base"
    CCY_DEFAULT: str = "USD"

    @classmethod
    def _current_price_extractor(cls, data):
        """Method for extracting current price"""
        raise NotImplementedError

    @classmethod
    def _current_bid_extractor(cls, data):
        """Method for extracting bid price"""
        raise NotImplementedError

    @classmethod
    def _current_ask_extractor(cls, data):
        """Method for extracting ask price"""
        raise NotImplementedError

    @classmethod
    def _current_orders_extractor(cls, data, max_qty=100):
        """Method for extracting orders"""
        raise NotImplementedError

    @classmethod
    def _current_ticker_extractor(cls, data):
        """Method for extracting ticker"""
        raise NotImplementedError

    @classmethod
    def get_current_price(cls, ccy=None, params=None, body=None, header=None):
        """Method for retrieving last price"""
        url = cls.PRICE_URL if hasattr(cls, "PRICE_URL") and cls.PRICE_URL else cls.TICKER_URL
        data = get_response(url, ccy, params, body, header)
        print(data)
        return cls._current_price_extractor(data)

    @classmethod
    def get_current_bid(cls, ccy=None, params=None, body=None, header=None):
        """Method for retrieving current bid price"""
        url = cls.BID_URL if hasattr(cls, "BID_URL") and cls.BID_URL is not None else cls.TICKER_URL
        data = get_response(url, ccy, params, body, header)
        return cls._current_bid_extractor(data)

    @classmethod
    def get_current_ask(cls, ccy=None, params=None, body=None, header=None):
        """Method for retrieving current ask price"""
        url = cls.ASK_URL if hasattr(cls, "ASK_URL") and cls.ASK_URL is not None else cls.TICKER_URL
        data = get_response(url, ccy, params, body, header)
        return cls._current_ask_extractor(data)

    @classmethod
    def get_current_ticker(cls, ccy=None, params=None, body=None, header=None):
        """Method for retrieving current ticker"""
        data = get_response(cls.TICKER_URL, ccy, params, body, header)
        return cls._current_ticker_extractor(data)

    @classmethod
    def get_current_orders(cls, ccy=None, params=None, body=None, header=None):
        """Method for retrieving current orders"""
        max_qty = 100
        data = get_response(cls.ORDER_BOOK_URL, ccy, params, body, header)
        return cls._current_orders_extractor(data, max_qty)
