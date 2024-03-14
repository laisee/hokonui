""" module for testing Zaif API """


import json
from sys import path
from unittest import TestCase

from hokonui.exchanges.zaif import Zaif as zf
from hokonui.utils.helpers import docstring_parameter as docparams

LIBPATH = "../hokonui"
if LIBPATH not in path:
    path.append(LIBPATH)


class TestZaif(TestCase):
    """Class for testing Zaif API"""

    @classmethod
    @docparams(zf.__name__, "setup")
    def setup(cls):
        """{0}.{1}"""
        print(__name__, ": TestClass.setup_class() ----------")

    @classmethod
    @docparams(zf.__name__, "teardown")
    def teardown(cls):
        """{0}.{1}"""
        print(__name__, ": TestClass.teardown_class() -------")

    @classmethod
    @docparams(zf.__name__, "name")
    def test_name(cls):
        """{0}.{1}"""

        assert zf.NAME == cls.__name__.replace("Test", "")

    @classmethod
    @docparams(zf.__name__, "price")
    def test_price(cls):
        """{0}.{1}"""

        assert float(zf.get_current_price(zf.CCY_DEFAULT)) > 0.00

    @classmethod
    @docparams(zf.__name__, "bid")
    def test_bid(cls):
        """{0}.{1}"""

        assert float(zf.get_current_bid(zf.CCY_DEFAULT)) > 0.00

    @classmethod
    @docparams(zf.__name__, "ask")
    def test_ask(cls):
        """{0}.{1}"""

        assert float(zf.get_current_ask(zf.CCY_DEFAULT)) > 0.00

    @classmethod
    @docparams(zf.__name__, "ticker")
    def test_ticker(cls):
        """{0}.{1}"""

        data = json.loads(zf.get_current_ticker(zf.CCY_DEFAULT))
        assert data["pair"] == zf.CCY_DEFAULT, "Ccy should be '%s', was '%s'" % (
            zf.CCY_DEFAULT,
            data["pair"],
        )
        assert float(data["ask"]) > 0.00, "ask should not be empty"
        assert float(data["bid"]) > 0.00, "bid should not be empty"
        assert float(data["bid"]) <= float(data["ask"]), "bid should be < ask"
        assert float(data["timestamp"]) > 0, "Timestamp should be > zero"

    @classmethod
    @docparams(zf.__name__, "orders")
    def test_orders(cls):
        """{0}.{1}"""

        orders = zf.get_current_orders(zf.CCY_DEFAULT)
        assert len(orders["asks"]) > 0, "Asks array should not be empty"
        assert len(orders["bids"]) > 0, "Bids array should not be empty"
        assert orders["source"] == "Zaif", "Source should be 'Zaif'"
        assert orders["ccy"] == zf.CCY_DEFAULT, "Ccy should be %s" % zf.CCY_DEFAULT
        assert float(orders["timestamp"]) > 0, "Timestamp should be > zero"


if __name__ == "__main__":
    pass
