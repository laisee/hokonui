''' module for testing Bitcoinaverage API '''
# pylint: disable=duplicate-code, line-too-long
import time
from hokonui.exchanges.base import Exchange
from hokonui.models.ticker import Ticker
from hokonui.utils.helpers import apply_format


class BitcoinAverage(Exchange):
    ''' Class for testing Bitcoinaverage API '''

    TICKER_URL = 'https://api.bitcoinaverage.com/ticker/global/%s/'
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
