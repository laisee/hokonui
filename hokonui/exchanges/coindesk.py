''' Module for testing Coindesk API '''
# pylint: disable=duplicate-code, line-too-long
from hokonui.utils.helpers import apply_format
from hokonui.utils.helpers import get_response
from hokonui.exchanges.base import Exchange as base


class CoinDesk(object):
    ''' Class for testing Coindesk API '''

    NAME = 'CoinDesk'

    @classmethod
    def get_current_price(cls, ccy=base.CCY_DEFAULT):
        ''' Method for retrieving current price '''
        url = 'https://api.coindesk.com/v1/bpi/currentprice/%s.json'
        data = get_response(url, ccy)
        price = data['bpi'][ccy]['rate']
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
        url = (
            'https://api.coindesk.com/v1/bpi/historical/close.json'
            '?start={}&end={}'.format(
                start, end
            )
        )
        return get_response(url, None)
