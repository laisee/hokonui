''' Module for testing CoinBasse API '''

from tests import *

libPath = '../hokonui'
if not libPath in sys.path: sys.path.append(libPath)

from hokonui.exchanges.base import Exchange as base
from hokonui.exchanges.coinfloor import Coinfloor as cfl


class TestCoinfloor(TestCase):
    ''' Class for testing Coinfloor API '''

    @classmethod
    @docparams(cfl.__name__,"setup")
    def setup(cls):
        ''' {0}.{1}'''
        print(__name__, ': TestClass.setup_class() ----------')

    @classmethod
    @docparams(cfl.__name__,"teardown")
    def teardown(cls):
        ''' {0}.{1}'''
        print(__name__, ': TestClass.teardown_class() -------')

    @classmethod
    @docparams(cfl.__name__,"name")
    def test_name(cls):
        ''' {0}.{1}'''
        ok_(cfl.NAME == cls.__name__.replace( 'Test', ''))

    @classmethod
    @docparams(cfl.__name__,"price")
    @unittest.skip("skip while fixing HBI url")
    def test_price(cls):
        ''' {0}.{1}'''
        ok_(float(cfl.get_current_price(base.CCY_DEFAULT, None, None, None)) > 0.00)

    @classmethod
    @docparams(cfl.__name__,"bid")
    @unittest.skip("skip while fixing HBI url")
    def test_bid(cls):
        ''' {0}.{1}'''
        ok_(float(cfl.get_current_bid(base.CCY_DEFAULT, None, None, None)) > 0.00)

    @classmethod
    @docparams(cfl.__name__,"ask")
    @unittest.skip("skip while fixing HBI url")
    def test_ask(cls):
        ''' {0}.{1}'''
        ok_(float(cfl.get_current_ask(base.CCY_DEFAULT, None)) > 0.00)

    @classmethod
    @docparams(cfl.__name__,"ticker")
    @unittest.skip("skip while fixing HBI url")
    def test_ticker(cls):
        ''' {0}.{1}'''
        data = json.loads(cfl.get_current_ticker(base.CCY_DEFAULT, None))
        ok_(data["pair"] == base.CCY_DEFAULT, "pair should be base.CCY_DEFAULT")
        ok_(float(data["ask"]) > 0.00, "ask should not be empty")
        ok_(float(data["bid"]) > 0.00, "bid should not be empty")
        ok_(float(data["bid"]) <= float(data["ask"]), "bid should be < ask")
        ok_(float(data["timestamp"]) > 0, "Timestamp should be > zero")

    @classmethod
    @docparams(cfl.__name__,"orders")
    @unittest.skip("skip while fixing HBI url")
    def test_orders(cls):
        ''' {0}.{1}'''
        orders = cfl.get_current_orders(base.CCY_DEFAULT)
        ok_(len(orders["asks"]) > 0, "Asks array should not be empty")
        ok_(len(orders["bids"]) > 0, "Bids array should not be empty")
        ok_(orders["source"] == "Coinfloor", "Source should be 'Coinfloor'")
        ok_(float(orders["timestamp"]) > 0, "Timestamp should be > zero")

if __name__ == '__main__':
    nose.runmodule()
