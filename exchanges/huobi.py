from exchanges.base import Exchange
from helpers import apply_format

class Huobi(Exchange):

    TICKER_URL = 'https://market.huobi.com/staticmarket/ticker_btc_json.js'

    @classmethod
    def _current_price_extractor(cls, data):
        return apply_format(data.get('ticker', {}).get('last'))

    @classmethod
    def _current_bid_extractor(cls, data):
        return apply_format(data.get('ticker', {}).get('buy'))

    @classmethod
    def _current_ask_extractor(cls, data):
        return apply_format(data.get('ticker', {}).get('sell'))
