from helpers import get_response, apply_format

class Coinapult(object):

    TICKER_URL = 'https://api.coinapult.com/api/ticker?market=%s_BTC'
    TICKER_LEVEL = [
        (50, 'small'),
        (250, 'medium'),
        (1000, 'large'),
        (2500, 'vip'),
        (5000, 'vip+')
    ]

    @classmethod
    def get_current_price(cls,ccy):
        url = cls.TICKER_URL.format(ccy)
        data = get_response(url,ccy)
        price = str(data['index'])
        return apply_format(price)

    @classmethod
    def get_current_bid(cls,ccy, btc_amount=0.1):
        url = cls.TICKER_URL.format(ccy)
        data = get_response(url,ccy)
        level = cls._pick_level(btc_amount) if btc_amount > 0 else 'small'
        price = str(data[level]['bid'])
        return apply_format(price)

    @classmethod
    def get_current_ask(cls,ccy, btc_amount=0.1):
        url = cls.TICKER_URL.format(ccy)
        data = get_response(url,ccy)
        level = cls._pick_level(btc_amount) if btc_amount > 0 else 'small'
        price = str(data[level]['ask'])
        return apply_format(price)

    @classmethod
    def _pick_level(cls, btc_amount):
        """
        Choose between small, medium, large, ... depending on the
        amount specified.
        """
        for size, level in cls.TICKER_LEVEL:
            if btc_amount < size:
                return level
        return cls.TICKER_LEVEL[-1][1]
