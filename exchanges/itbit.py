from exchanges.base import Exchange
from helpers import apply_format                                 

class Itbit(Exchange):

    TICKER_URL = 'https://api.itbit.com/v1/markets/XBT%s/ticker'

    @classmethod
    def _current_price_extractor(cls, data):
        return apply_format(data.get('lastPrice'))

    @classmethod
    def _current_bid_extractor(cls, data):
        return apply_format(data.get('bid'))

    @classmethod
    def _current_ask_extractor(cls, data):
        return apply_format(data.get('ask'))
