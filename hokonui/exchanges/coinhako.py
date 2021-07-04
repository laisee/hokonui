''' Module for Exchange base class '''
# pylint: disable=duplicate-code, line-too-long

from hokonui.exchanges.base import Exchange as Base
from hokonui.models.ticker import Ticker
from hokonui.utils.helpers import apply_format, get_response


class Coinhako(Base):
    ''' Class Exchange base class for all exchanges '''

    TICKER_URL: str = 'https://www.coinhako.com/api/v1/price/currency/BTC%s'
    ORDER_BOOK_URL: str = ""
    NAME: str = 'Coinhako'
    CCY_DEFAULT: str = 'USD'

    @classmethod
    def _current_price_extractor(cls, data):
        ''' Method for extracting current price '''
        return apply_format((float(data["data"].get('buy_price')) +
                             float(data["data"].get('sell_price'))) / 2.00)

    @classmethod
    def _current_bid_extractor(cls, data):
        ''' Method for extracting bid price '''
        return apply_format(data["data"].get('buy_price'))

    @classmethod
    def _current_ask_extractor(cls, data):
        ''' Method for extracting ask price '''
        return apply_format(data["data"].get('sell_price'))

    @classmethod
    def _current_orders_extractor(cls, data, max_qty=100):
        ''' Method for extracting orders '''
        raise NotImplementedError("orders API not available for CoinHako")

    @classmethod
    def _current_ticker_extractor(cls, data):
        ''' Method for extracting ticker '''
        bid = apply_format(data["data"].get('buy_price'))
        ask = apply_format(data["data"].get('sell_price'))
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
