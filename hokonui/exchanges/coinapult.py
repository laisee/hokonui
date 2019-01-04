''' Module for testing Coinapult API '''
# pylint: disable=duplicate-code, line-too-long

from hokonui.utils.helpers import get_response, apply_format
from hokonui.models.ticker import Ticker
from hokonui.exchanges.base import Exchange as Base


class Coinapult(Base):
    ''' Class for testing Coinapult API '''

    TICKER_URL = 'https://api.coinapult.com/api/ticker?market=%s_BTC'
    TICKER_LEVEL = [
        (50, 'small'),
        (250, 'medium'),
        (1000, 'large'),
        (2500, 'vip'),
        (5000, 'vip+')
    ]
    NAME = 'Coinapult'

    @classmethod
    def get_current_price(cls, ccy):
        ''' method for testing last price '''
        url = cls.TICKER_URL.format(ccy)
        data = get_response(url, ccy)
        price = str(data['index'])
        return apply_format(price)

    @classmethod
    def get_current_bid(cls, ccy, btc_amount=0.1):
        ''' method for testing current bid price '''
        url = cls.TICKER_URL.format(ccy)
        data = get_response(url, ccy)
        level = cls._pick_level(btc_amount) if btc_amount > 0 else 'small'
        price = str(data[level]['bid'])
        return apply_format(price)

    @classmethod
    def get_current_ask(cls, ccy, btc_amount=0.1):
        ''' method for testing current ask price '''
        url = cls.TICKER_URL.format(ccy)
        data = get_response(url, ccy)
        level = cls._pick_level(btc_amount) if btc_amount > 0 else 'small'
        price = str(data[level]['ask'])
        return apply_format(price)

    @classmethod
    def _current_ticker_extractor(cls, ccy, data, btc_amount=0):
        ''' method for testing current ticker '''
        url = cls.TICKER_URL.format(ccy)
        data = get_response(url, ccy)
        level = cls._pick_level(btc_amount) if btc_amount > 0 else 'small'
        ask = apply_format(str(data[level]['ask']))
        bid = apply_format(str(data[level]['bid']))
        return Ticker(ccy, bid, ask).toJSON()

    @classmethod
    def get_current_orders(cls, ccy):
        ''' method for testing current orders '''
        raise ValueError("not implemented for this class using ccy %s" % ccy)

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
