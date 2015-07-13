from decimal import Decimal
from exchanges.base import Exchange


class MexBtc(Exchange):

    TICKER_URL = 'https://public-api.mexbt.com/v1/ticker'
    BODY = '{"productPair": "BTCUSD"}'

    @classmethod
    def _current_price_extractor(cls, data):
        return format(Decimal(data.get('last')),'.6f')

    @classmethod
    def _current_bid_extractor(cls, data):
        return format(Decimal(data.get('bid')),'.6f')

    @classmethod
    def _current_ask_extractor(cls, data):
        return format(Decimal(data.get('ask')),'.6f')
