""" module for testing liquid n API """

import json
from sys import path
from unittest import TestCase

import pytest

from hokonui.exchanges.base import Exchange as base
from hokonui.exchanges.liquid import Liquid as liquid
from hokonui.utils.helpers import docstring_parameter as docparams

LIBPATH = "../hokonui"
if LIBPATH not in path:
    path.append(LIBPATH)


class TestLiquid(TestCase):
    """Class for testing Liquid API"""

    @classmethod
    @docparams(liquid.__name__, "setup")
    def setup(cls):
        """{0}.{1}"""

        print(__name__, ": TestClass.setup_class() ----------")

    @classmethod
    @docparams(liquid.__name__, "teardown")
    def teardown(cls):
        """{0}.{1}"""

        print(__name__, ": TestClass.teardown_class() -------")

    @classmethod
    @docparams(liquid.__name__, "name")
    def test_name(cls):
        """{0}.{1}"""

        assert liquid.NAME == cls.__name__.replace("Test", "")

    @classmethod
    @docparams(liquid.__name__, "price")
    def test_price(cls):
        """{0}.{1}"""

        assert float(liquid.get_current_price(base.CCY_DEFAULT)) > 0.00

    @classmethod
    @docparams(liquid.__name__, "bid")
    def test_bid(cls):
        """{0}.{1}"""

        assert float(liquid.get_current_bid(base.CCY_DEFAULT)) > 0.00

    @classmethod
    @docparams(liquid.__name__, "ask")
    def test_ask(cls):
        """{0}.{1}"""

        assert float(liquid.get_current_ask(base.CCY_DEFAULT)) > 0.00

    @classmethod
    @docparams(liquid.__name__, "ticker")
    def test_ticker(cls):
        """{0}.{1}"""

        data = json.loads(liquid.get_current_ticker(base.CCY_DEFAULT))
        assert data["pair"] == base.CCY_DEFAULT, "shd be '%s'" % base.CCY_DEFAULT
        assert float(data["ask"]) > 0.00, "ask should not be empty"
        assert float(data["bid"]) > 0.00, "bid should not be empty"
        assert float(data["bid"]) <= float(data["ask"]), "bid should be < ask"
        assert float(data["timestamp"]) > 0, "Timestamp should be > zero"

    @classmethod
    @docparams(liquid.__name__, "orders")
    @pytest.mark.skip("Order book not available to public")
    def test_orders(cls):
        """{0}.{1}"""

        ccy_id = cls.ccy_to_id(base.CCY_DEFAULT)
        orders = liquid.get_current_orders(ccy_id)
        assert len(orders["asks"]) > 0, "Asks array should not be empty"
        assert len(orders["bids"]) > 0, "Bids array should not be empty"
        assert orders["source"] == "Liquid", "Source should be 'Liquid'"
        assert float(orders["timestamp"]) > 0, "Timestamp should be > zero"

    @staticmethod
    def ccy_to_id(ccy):
        """static method for converting CCY string to ID value"""

        ccyid = -1
        if ccy == "USD":
            ccyid = 1
        elif ccy == "EUR":
            ccyid = 3
        elif ccy == "JPY":
            ccyid = 5
        elif ccy == "SGD":
            ccyid = 7
        elif ccy == "HKD":
            ccyid = 9
        elif ccy == "IDR":
            ccyid = 11
        elif ccy == "AUD":
            ccyid = 13
        elif ccy == "PHP":
            ccyid = 15
        elif ccy == "CNY":
            ccyid = 17
        elif ccy == "INR":
            ccyid = 18
        else:
            raise ValueError("Invalid Currency : %s " % ccy)
        return ccyid


if __name__ == "__main__":
    pass
