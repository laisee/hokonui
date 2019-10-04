''' module for testing Bitcoinaverage API '''
# pylint: disable=duplicate-code, line-too-long
import time

from hokonui.exchanges.base import Exchange as Base
from hokonui.models.ticker import Ticker
from hokonui.utils.helpers import apply_format


class BitcoinAverage(Base):
    '''
    Class for testing Bitcoinaverage API
    {
    "24h_avg": 748.64,
    "ask": 751.73,
    "bid": 750.38,
    "last": 751.2,
    "timestamp": "Thu, 24 Nov 2016 00:48:23 -0000",
    "volume_btc": 42523.1,
    "volume_percent": 56.36
     }
    '''

    TICKER_URL = 'https://apiv2.bitcoinaverage.com/indices/global/ticker/BTC%s'
    NAME = 'BitcoinAverage'

    @classmethod
    def _current_price_extractor(cls, data):
        ''' current price extractor '''
        return apply_format(data.get('last'))

    @classmethod
    def _current_bid_extractor(cls, data):
        ''' current bid price extractor '''
        return apply_format(data.get('bid'))

    @classmethod
    def _current_ask_extractor(cls, data):
        ''' current ask price extractor '''
        return apply_format(data.get('ask'))

    @classmethod
    def _current_ticker_extractor(cls, data):
        ''' current ticker extractor '''
        bid = apply_format(data.get('bid'))
        ask = apply_format(data.get('ask'))
        return Ticker(cls.CCY_DEFAULT, bid, ask).toJSON()

    @classmethod
    def _current_orders_extractor(cls, data, max_qty=3):
        raise NotImplementedError

    @classmethod
    def current_volume_extractor(cls, data):
        ''' current volume extractor '''
        vol = {}
        vol["source"] = cls.NAME
        vol["quantity"] = data.get('volume_btc')
        vol["timestamp"] = str(int(time.time()))
        return vol
