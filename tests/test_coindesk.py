""" Module for testing CoinDesk API """


from sys import path
from unittest import TestCase
import unittest

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

        assert float(coin.get_past_price()) > 0.00

    @classmethod
    @docparams(coin.__name__, "historical_data")
    def test_historical_data(cls):
        """{0}.{1}"""

        ts = 1645160620
        data = coin.get_historical_data(ts)
        assert data is not None, f"Error - no historical data found for BTC-USD at {ts}"
        assert len(data) > 0, f"Error - no historical data found for BTC-USD at {ts}"
        assert data["Data"][0]["OPEN"] is not None and float(data["Data"][0]["OPEN"]) > 0.00,f"Error - no OPEN price found in historical data @ {ts}"
        assert data["Data"][0]["HIGH"] is not None and float(data["Data"][0]["HIGH"]) > 0.00,f"Error - no HIGH price found in historical data @ {ts}"
        assert data["Data"][0]["LOW"] is not None and float(data["Data"][0]["LOW"]) > 0.00,f"Error - no LOW price found in historical data @ {ts}"
        assert data["Data"][0]["CLOSE"] is not None and float(data["Data"][0]["CLOSE"]) > 0.00,f"Error - no CLOSE price found in historical data @ {ts}"

if __name__ == "__main__":
    pass
