""" Module for testing Bitfinex API """
# pylint: disable=duplicate-code, line-too-long

import time

from hokonui.exchanges.base import Exchange as Base
from hokonui.models.ticker import Ticker
from hokonui.utils.helpers import apply_format, apply_format_level


class CryptoDotCom(Base):
    """class for testing CryptoDotComitfinex public information API"""

    TICKER_URL = "https://api.crypto.com/exchange/v1/public/get-tickers?instrument_name=BTCUSD-PERP"
    ORDER_BOOK_URL = "https://api.crypto.com/exchange/v1/public/get-book?instrument_name=BTCUSD-PERP&depth=10"
    NAME = "CryptoDotCom"

    @classmethod
    def _current_price_extractor(cls, data):
        """Method for extracting current price"""
        return apply_format(data["result"]["data"][0]["l"])

    @classmethod
    def _current_bid_extractor(cls, data):
        """Method for extracting bid price"""
        return apply_format(data["result"]["data"][0]["b"])

    @classmethod
    def _current_ask_extractor(cls, data):
        """Method for extracting ask price"""
        return apply_format(data["result"]["data"][0]["k"])

    @classmethod
    def _current_ticker_extractor(cls, data):
        """Method for extracting ticker"""
        bid = apply_format(data["result"]["data"][0]["b"])
        ask = apply_format(data["result"]["data"][0]["k"])
        return Ticker("BTCUSD", bid, ask).to_json()

    @classmethod
    def _current_orders_extractor(cls, data, max_qty=3):
        """Method for extracting orders"""
        orders = {}
        bids = {}
        asks = {}
        buymax = 0
        sellmax = 0
        for level in data["result"]["data"][0]["bids"]:
            if buymax > max_qty:
                continue
            else:
                bids[apply_format_level(level[0])] = "{:.8f}".format(float(level[1]))
            buymax = buymax + float(level[1])

        for level in data["result"]["data"][0]["asks"]:
            if sellmax > max_qty:
                continue
            else:
                asks[apply_format_level(level[0])] = "{:.8f}".format(float(level[1]))
            sellmax = sellmax + float(level[1])

        orders["source"] = "Bitfinex"
        orders["bids"] = bids
        orders["asks"] = asks
        orders["timestamp"] = str(int(time.time()))
        return orders
