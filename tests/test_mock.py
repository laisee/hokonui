""" Module for testing Mock exchange """

import json
from sys import path
from unittest import TestCase

from hokonui.exchanges.mock import Mock as mock
from hokonui.utils.helpers import docstring_parameter as docparams

LIBPATH = "../hokonui"
if LIBPATH not in path:
    path.append(LIBPATH)


class TestMock(TestCase):
    """Class for testing Mock exchange"""

    @classmethod
    @docparams(mock.__name__, "setup")
    def setUp(cls):
        """{0}.{1}"""

        print(__name__, ": TestClass.setup_class() ----------")

    @classmethod
    @docparams(mock.__name__, "teardown")
    def tearDown(cls):
        """{0}.{1}"""

        print(__name__, ": TestClass.teardown_class() -------")

    @classmethod
    @docparams(mock.__name__, "name")
    def test_name(cls):
        """{0}.{1}"""

        assert mock.NAME == cls.__name__.replace(
            "Test", ""
        ), "Name should be '%s', was '%s'" % (mock.NAME, cls.__name__)

    @classmethod
    @docparams(mock.__name__, "price")
    def test_price(cls):
        """{0}.{1}"""

        assert (
            float(mock.get_current_price(mock.CCY_DEFAULT)) == mock.MOCK_PRICE
        ), "Invalid price: should be %s, was %s" % (
            mock.MOCK_PRICE,
            mock.get_current_price(mock.CCY_DEFAULT),
        )

    @classmethod
    @docparams(mock.__name__, "bid")
    def test_bid(cls):
        """{0}.{1}"""

        assert (
            float(mock.get_current_bid(mock.CCY_DEFAULT)) == mock.MOCK_PRICE
        ), "Invalid price: should be %s, was %s" % (
            mock.MOCK_PRICE,
            mock.get_current_price(mock.CCY_DEFAULT),
        )

    @classmethod
    @docparams(mock.__name__, "ask")
    def test_ask(cls):
        """{0}.{1}"""

        assert (
            float(mock.get_current_ask(mock.CCY_DEFAULT)) == mock.MOCK_PRICE
        ), "Invalid price: should be %s, was %s" % (
            mock.MOCK_PRICE,
            mock.get_current_price(mock.CCY_DEFAULT),
        )

    @classmethod
    @docparams(mock.__name__, "ticker")
    def test_ticker(cls):
        """{0}.{1}"""

        data = json.loads(mock.get_current_ticker(mock.CCY_DEFAULT))
        assert (
            data["pair"] == mock.CCY_DEFAULT
        ), "currency pair should be '%s', was %s" % (mock.CCY_DEFAULT, data["pair"])
        assert (
            float(data["ask"]) == mock.MOCK_PRICE
        ), "ask price should be %s, was %s" % (mock.MOCK_PRICE, float(data["ask"]))
        assert (
            float(data["bid"]) == mock.MOCK_PRICE
        ), "bid price should be %s, was %s" % (mock.MOCK_PRICE, float(data["bid"]))
        assert float(data["bid"]) <= float(
            data["ask"]
        ), "bid price %s should be < ask price %s" % (
            float(data["ask"]),
            float(data["ask"]),
        )
        assert float(data["timestamp"]) > 0, (
            "Timestamp should be > zero, value was %s" % data["timestamp"]
        )

    @classmethod
    @docparams(mock.__name__, "orders")
    def test_orders(cls):
        """{0}.{1}"""

        orders = mock.get_current_orders(mock.CCY_DEFAULT)
        # test Asks
        assert len(orders["asks"]) > 0, "Asks array should not be empty"
        assert float(orders["asks"]["1.23"]) == float(
            mock.MOCK_ASK_QTY
        ), "Asks order qty @ price 1.23 should be %s, was %s" % (
            mock.MOCK_ASK_QTY,
            orders["asks"]["1.23"],
        )

        # test Bids
        assert len(orders["bids"]) > 0, "Bids array should not be empty"
        assert float(orders["bids"]["1.23"]) == float(
            mock.MOCK_BID_QTY
        ), "Bids order qty @ price 1.23 should be %s, was %s" % (
            mock.MOCK_BID_QTY,
            orders["asks"]["1.23"],
        )

        # test other data
        assert orders["source"] == "Mock", (
            "Source should be 'Mock', was %s" % orders["source"]
        )
        assert float(orders["timestamp"]) > 0, (
            "Timestamp should be > zero, value was %s" % orders["timestamp"]
        )


if __name__ == "__main__":
    pass
