''' Module for testing Mock Exchange API '''
# pylint: disable=duplicate-code, line-too-long

from hokonui.exchanges.base import Exchange as Base
from hokonui.utils.helpers import apply_format
from hokonui.models.ticker import Ticker


class MockExchange(Base):
    ''' Class for testing Mock Exchange API '''

    TICKER_URL = 'https://api.mock.com/XBT%s/ticker'
    ORDER_BOOK_URL = 'https://api.mock.com/XBT%s/order_book'
    NAME = 'MockExchange'

    @classmethod
    def _current_price_extractor(cls, data):
        return apply_format(data.get('lastPrice'))

    @classmethod
    def _current_bid_extractor(cls, data):
        return apply_format(data.get('bid'))

    @classmethod
    def _current_ask_extractor(cls, data):
        return apply_format(data.get('ask'))

    @classmethod
    def _current_ticker_extractor(cls, data):
        return Ticker(cls.CCY_DEFAULT, apply_format(data.get('bid')), apply_format(data.get('ask'))).toJSON()

    @classmethod
    def _current_orders_extractor(cls, data, max_qty=3):
        raise ValueError('Not implemented yet')
