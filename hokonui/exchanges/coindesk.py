from hokonui.utils.helpers import get_datetime, get_response, apply_format

class CoinDesk(object):

    NAME = 'CoinDesk'

    @classmethod
    def get_current_price(cls,ccy='USD'):
        url = 'https://api.coindesk.com/v1/bpi/currentprice/%s.json'
        data = get_response(url,ccy)
        price = data['bpi'][ccy]['rate']
        return apply_format(price)

    @classmethod
    def get_past_price(cls,date):
        data = cls._get_historical_data(date)
        price = data['bpi'][date]
        return apply_format(str(price))

    @classmethod
    def _get_historical_data(cls,start,end=None):
        if not end:
            end = start
        url = (
            'https://api.coindesk.com/v1/bpi/historical/close.json'
            '?start={}&end={}'.format(
                start, end
            )
        )
        return get_response(url,None)
