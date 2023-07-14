""" Module for testing CoinDesk API """


from sys import path
from unittest import TestCase

from hokonui.exchanges.coindesk import CoinDesk as coin
from hokonui.utils.helpers import docstring_parameter as docparams

LIBPATH = "../hokonui"
if LIBPATH not in path:
    path.append(LIBPATH)


class TestCoinDesk(TestCase):
    """Class for testing Coindesk API"""

    @classmethod
    @docparams(coin.__name__, "name")
    def test_name(cls):
        """{0}.{1}"""

        assert coin.NAME == cls.__name__.replace("Test", "")

    @classmethod
    @docparams(coin.__name__, "price")
    def test_price(cls):
        """{0}.{1}"""

        assert float(coin.get_current_price()) > 0.00

    @classmethod
    @docparams(coin.__name__, "past_price")
    def test_past_price(cls):
        """{0}.{1}"""

        assert float(coin.get_past_price("2015-07-05")) > 0.00


if __name__ == "__main__":
    nose.runmodule()
