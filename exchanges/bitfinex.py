from exchanges.base import Exchange
from helpers import apply_format

class Bitfinex(Exchange):

    TICKER_URL = 'https://api.bitfinex.com/v1/pubticker/btcusd'

    @classmethod
    def _current_price_extractor(cls, data):
        return apply_format(data.get('last_price'))

    @classmethod
    def _current_bid_extractor(cls, data):
        return apply_format(data.get('bid'))

    @classmethod
    def _current_ask_extractor(cls, data):
        return apply_format(data.get('ask'))
