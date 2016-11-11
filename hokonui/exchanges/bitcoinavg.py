import json
import time
from hokonui.exchanges.base import Exchange
from hokonui.models.ticker import Ticker
from hokonui.utils.helpers import get_datetime, get_response, apply_format

class BitcoinAverage(Exchange):

    TICKER_URL = 'https://api.bitcoinaverage.com/ticker/global/%s/'
    NAME = 'BitcoinAverage'

    @classmethod
    def _current_price_extractor(cls, data):
        return apply_format(data.get('last'))

    @classmethod
    def _current_bid_extractor(cls, data):
        return apply_format(data.get('bid'))

    @classmethod
    def _current_ask_extractor(cls, data):
        return apply_format(data.get('ask'))

    @classmethod
    def _current_ticker_extractor(cls, data):
        return Ticker(cls.CCY_DEFAULT,apply_format(data.get('bid')), apply_format(data.get('ask'))).toJSON()

    @classmethod
    def _current_volume_extractor(cls,data):
        vol = {}
        vol["source"] = cls.NAME
        vol["quantity"] = data.get('volume_btc')
        vol["timestamp"] = str(int(time.time()))
        return vol
