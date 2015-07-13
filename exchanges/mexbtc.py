from decimal import Decimal
from exchanges.base import Exchange
from helpers import apply_format

class MexBtc(Exchange):

    TICKER_URL = 'https://public-api.mexbt.com/v1/ticker'
    BODY = '{"productPair": "BTCUSD"}'

    @classmethod
    def _current_price_extractor(cls, data):
        return apply_format(data.get('last'))

    @classmethod
    def _current_bid_extractor(cls, data):
        return apply_format(data.get('bid'))

    @classmethod
    def _current_ask_extractor(cls, data):
        return apply_format(data.get('ask'))
