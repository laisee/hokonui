import time
from hokonui.exchanges.base import Exchange
from hokonui.utils.helpers import apply_format, apply_format_level

class Huobi(Exchange):

    TICKER_URL = 'https://market.huobi.com/staticmarket/ticker_btc_json.js'
    ORDER_BOOK_URL = 'http://api.huobi.com/staticmarket/detail_btc_json.js'
    # = '{"total":118268152.7731,"p_high":1720.58,"p_open":1691.22,"p_new":1689,"p_low":1651.08,"top_buy":[{"amount":14.1121,"level":0,"price":1689,"accu":14.1121},'
    NAME = 'Huobi'

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
    def _current_orders_extractor(cls,data, max_qty):
        orders = {}
        bids = {}
        asks = {}
        buyMax = 0
        sellMax = 0
        for level in data["top_buy"]:
            if buyMax > max_qty:
               continue
            else:
               bids[apply_format_level(level["price"])] = "{:.8f}".format(float(level["amount"]))
            buyMax = buyMax + float(level["amount"])

        for level in data["top_sell"]:
            if sellMax > max_qty:
                continue
            else:
               asks[apply_format_level(level["price"])] = "{:.8f}".format(float(level["amount"]))
            sellMax = sellMax + float(level["amount"])
        orders["source"] = "Huobi"
        orders["bids"] = bids
        orders["asks"] = asks
        orders["timestamp"] = str(int(time.time()))
        return orders
