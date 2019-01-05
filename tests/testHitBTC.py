''' Module for testing HitBTC exchange '''

from tests import *

libPath = '../hokonui'
if not libPath in sys.path: sys.path.append(libPath)

from hokonui.exchanges.base import Exchange as base
from hokonui.exchanges.hitbtc import HitBTC as bin


class TestHitBTC(TestCase):
    ''' Class for testing HitBTC exchange '''

    @classmethod
    @docparams(bin.__name__,"setup")
    def setUp(cls):
        ''' {0}.{1}'''

        print(__name__, ': TestClass.setup_class() ----------')

    @classmethod
    @docparams(bin.__name__,"teardown")
    def tearDown(cls):
        ''' {0}.{1}'''

        print(__name__, ': TestClass.teardown_class() -------')

    @classmethod
    @docparams(bin.__name__,"name")
    def test_name(cls):
        ''' {0}.{1} '''

        ok_(bin.NAME == cls.__name__.replace( 'Test', ''), "Name should be '%s', was '%s'" % (bin.NAME, cls.__name__))

    @classmethod
    @docparams(bin.__name__,"price")
    def test_price(cls):
        ''' {0}.{1} '''

        ok_(float(bin.get_current_price(bin.CCY_DEFAULT)) > 0.00)

    @classmethod
    @docparams(bin.__name__,"bid")
    def test_bid(cls):
        ''' {0}.{1} '''

        ok_(float(bin.get_current_bid(bin.CCY_DEFAULT)) > 0.00)

    @classmethod
    @docparams(bin.__name__,"ask")
    def test_ask(cls):
        ''' {0}.{1} '''

        ok_(float(bin.get_current_ask(bin.CCY_DEFAULT)) > 0.00)

    @classmethod
    @docparams(bin.__name__,"ticker")
    def test_ticker(cls):
        ''' {0}.{1} '''

        data = json.loads(bin.get_current_ticker(bin.CCY_DEFAULT))
        ok_(data["pair"] == bin.CCY_DEFAULT, "should be '%s'" % bin.CCY_DEFAULT)
        ok_(float(data["ask"]) > 0.00, "ask should not be empty")
        ok_(float(data["bid"]) > 0.00, "bid should not be empty")
        ok_(float(data["bid"]) <= float(data["ask"]), "bid should be < ask")
        ok_(float(data["timestamp"]) > 0, "Timestamp should be > zero")

    @classmethod
    @docparams(bin.__name__,"orders")
    def test_orders(cls):
        ''' {0}.{1} '''

        orders = bin.get_current_orders(bin.CCY_DEFAULT)
        ok_(len(orders["asks"]) > 0, "Asks array should not be empty")
        ok_(len(orders["bids"]) > 0, "Bids array should not be empty")
        ok_(orders["source"] == "HitBTC", "Source should be 'HitBTC'")
        ok_(float(orders["timestamp"]) > 0, "Timestamp should be > zero")

if __name__ == '__main__':
    nose.runmodule()
