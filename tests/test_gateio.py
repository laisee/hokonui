""" Module for testing GateIo exchange """

import json
from sys import path
from unittest import TestCase

from hokonui.exchanges.gateio import GateIo as gate
from hokonui.utils.helpers import docstring_parameter as docparams

LIBPATH = "../hokonui"
if LIBPATH not in path:
    path.append(LIBPATH)


class TestGateIo(TestCase):
    """Class for testing GateIo exchange"""

    @classmethod
    @docparams(gate.__name__, "setup")
    def setUp(cls):
        """{0}.{1}"""

        print(__name__, ": TestClass.setup_class() ----------")

    @classmethod
    @docparams(gate.__name__, "teardown")
    def tearDown(cls):
        """{0}.{1}"""

        print(__name__, ": TestClass.teardown_class() -------")

    @classmethod
    @docparams(gate.__name__, "name")
    def test_name(cls):
        """{0}.{1}"""

        assert gate.NAME == cls.__name__.replace(
            "Test", ""
        ), "Name should be '%s', was '%s'" % (gate.NAME, cls.__name__)

    @classmethod
    @docparams(gate.__name__, "price")
    def test_price(cls):
        """{0}.{1}"""

        assert float(gate.get_current_price(gate.CCY_DEFAULT)) > 0.00

    @classmethod
    @docparams(gate.__name__, "bid")
    def test_bid(cls):
        """{0}.{1}"""

        assert float(gate.get_current_bid(gate.CCY_DEFAULT)) > 0.00

    @classmethod
    @docparams(gate.__name__, "ask")
    def test_ask(cls):
        """{0}.{1}"""

        assert float(gate.get_current_ask(gate.CCY_DEFAULT)) > 0.00

    @classmethod
    @docparams(gate.__name__, "ticker")
    def test_ticker(cls):
        """{0}.{1}"""

        data = json.loads(gate.get_current_ticker(gate.CCY_DEFAULT))
        assert data["pair"] == gate.CCY_DEFAULT, "should be '%s'" % gate.CCY_DEFAULT
        assert float(data["ask"]) > 0.00, "ask should not be empty"
        assert float(data["bid"]) > 0.00, "bid should not be empty"
        assert float(data["bid"]) <= float(data["ask"]), "bid should be < ask"
        assert float(data["timestamp"]) > 0, "Timestamp should be > zero"

    @classmethod
    @docparams(gate.__name__, "orders")
    def test_orders(cls):
        """{0}.{1}"""

        orders = gate.get_current_orders(gate.CCY_DEFAULT)
        assert len(orders["asks"]) > 0, "Asks array should not be empty"
        assert len(orders["bids"]) > 0, "Bids array should not be empty"
        assert orders["source"] == "GateIo", "Source should be 'GateIo'"
        assert float(orders["timestamp"]) > 0, "Timestamp should be > zero"


if __name__ == "__main__":
    pass
