import time
from exchanges.base import Exchange
from utils.helpers import apply_format, apply_format_level

class OKCoin(Exchange):

    TICKER_URL = 'https://www.okcoin.com/api/ticker.do?ok=1'
    ORDER_BOOK_URL = 'https://www.okcoin.com/api/v1/depth.do?symbol=btc_usd&size=10'

    @classmethod
    def _current_price_extractor(cls, data):
        return apply_format(data.get('ticker', {}).get('last'))

    @classmethod
    def _current_bid_extractor(cls, data):
        return apply_format(data.get('ticker', {}).get('buy'))

    @classmethod
    def _current_ask_extractor(cls, data):
        return apply_format(data.get('ticker', {}).get('sell'))

    @classmethod
    def _current_orders_extractor(cls,data,max_qty=3):
        orders = {}
        bids = {}
        asks = {}
        buyMax = 0
        sellMax = 0
        for level in data["bids"]:
            if buyMax > max_qty:
                pass
            else:
                bids[apply_format_level(level[0])] = "{:.8f}".format(float(level[1]))
            buyMax = buyMax + float(level[1])

        for level in data["asks"]:
            if sellMax > max_qty:
                pass
            else:
                asks[apply_format_level(level[0])] = "{:.8f}".format(float(level[1]))
            sellMax = sellMax + float(level[1])

        orders["Source"] = "OKCoin"
        orders["Bids"] = bids
        orders["Asks"] = asks
        orders["Timestamp"] = str(int(time.time()))
        raise ValueError(str(orders))
        return orders
