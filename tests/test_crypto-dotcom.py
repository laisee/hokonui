""" Module for testing Birfinex API """

import json
from sys import path
from unittest import TestCase

from hokonui.exchanges.base import Exchange as base
from hokonui.exchanges.cryptodotcom import CryptoDotCom as cdc
from hokonui.utils.helpers import docstring_parameter as docparams

LIBPATH = "../hokonui"
if LIBPATH not in path:
    path.append(LIBPATH)


class TestCryptoDotCom(TestCase):
    """Class for testing Crypto.com API"""

    @classmethod
    @docparams(cdc.__name__, "name")
    def test_name(cls):
        """{0}.{1}"""
        assert cdc.NAME == cls.__name__.replace("Test", "")

    @classmethod
    @docparams(cdc.__name__, "price")
    def test_price(cls):
        """{0}.{1}"""
        assert float(cdc.get_current_price()) > 0.00

    @classmethod
    @docparams(cdc.__name__, "bid")
    def test_bid(cls):
        """{0}.{1}"""
        assert float(cdc.get_current_bid()) > 0.00

    @classmethod
    @docparams(cdc.__name__, "ask")
    def test_ask(cls):
        """{0}.{1}"""
        assert float(cdc.get_current_ask()) > 0.00

    @classmethod
    @docparams(cdc.__name__, "ticker")
    def test_ticker(cls):
        """{0}.{1}"""
        data = json.loads(cdc.get_current_ticker())
        assert float(data["ask"]) > 0.00, "ask should not be empty"
        assert float(data["bid"]) > 0.00, "bid should not be empty"
        assert float(data["bid"]) <= float(data["ask"]), "bid should be < ask"
        assert float(data["timestamp"]) > 0, "Timestamp should be > zero"

    @classmethod
    @docparams(cdc.__name__, "orders")
    def test_orders(cls):
        """{0}.{1}"""
        orders = cdc.get_current_orders()
        assert len(orders["asks"]) > 0, "Asks array should not be empty"
        assert len(orders["bids"]) > 0, "Bids array should not be empty"
        assert orders["source"] == "Bitfinex", "Source should be 'Bitfinex'"
        assert float(orders["timestamp"]) > 0, "Timestamp should be > zero"


if __name__ == "__main__":
    pass
