''' Module for testing Coindesk API '''
# pylint: disable=duplicate-code, line-too-long

from hokonui.utils.helpers import apply_format
from hokonui.utils.helpers import get_response
from hokonui.exchanges.base import Exchange as Base


class CoinDesk(Base):
    ''' Class for testing Coindesk API '''

    NAME = 'CoinDesk'

    @classmethod
    def _current_ticker_extractor(cls, data):
        ''' Method for extracting ticker '''

    @classmethod
    def _current_price_extractor(cls, data):
        ''' Method for extracting current price '''

    @classmethod
    def _current_bid_extractor(cls, data):
        ''' Method for extracting bid price '''

    @classmethod
    def _current_ask_extractor(cls, data):
        ''' Method for extracting ask price '''

    @classmethod
    def _current_orders_extractor(cls, data, max_qty=100):
        ''' Method for extracting ask price '''

    @classmethod
    def get_current_price(cls, ccy=Base.CCY_DEFAULT, params=None, body=None, header=None):
        ''' Method for retrieving current price '''
        url = 'https://api.coindesk.com/v1/bpi/currentprice/%s.json'
        data = get_response(url, ccy)
        price = data['bpi'][ccy]['rate_float']
        return apply_format(price)

    @classmethod
    def get_past_price(cls, date):
        ''' Method for retrieving past price '''
        data = cls._get_historical_data(date)
        price = data['bpi'][date]
        return apply_format(str(price))

    @classmethod
    def _get_historical_data(cls, start, end=None):
        ''' Method for retrieving historical data '''
        if not end:
            end = start
        url = ('https://api.coindesk.com/v1/bpi/historical/close.json'
               '?start={}&end={}'.format(start, end))
        return get_response(url, None)
