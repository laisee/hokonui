from hokonui.exchanges.base import Exchange
from hokonui.utils.helpers import apply_format                                 

class MockExchange(Exchange):

    TICKER_URL = 'https://api.mock.com/v1/markets/XBT%s/ticker'
    NAME = 'MockExchange'

    @classmethod
    def _current_price_extractor(cls, data):
        return apply_format(data.get('lastPrice'))

    @classmethod
    def _current_bid_extractor(cls, data):
        return apply_format(data.get('bid'))

    @classmethod
    def _current_ask_extractor(cls, data):
        return apply_format(data.get('ask'))
