from exchanges.base import Exchange
from helpers import apply_format

class Bitstamp(Exchange):

    TICKER_URL = 'https://bitstamp.net/api/ticker/'

    @classmethod
    def _current_price_extractor(cls, data):
        return apply_format(data.get('last'))

    @classmethod
    def _current_bid_extractor(cls, data):
        return apply_format(data.get('bid'))

    @classmethod
    def _current_ask_extractor(cls, data):
        return apply_format(data.get('ask'))
