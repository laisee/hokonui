''' Module for testing BTCE exchange '''

from tests import *

libPath = '../hokonui'
if not libPath in sys.path: sys.path.append(libPath)

from hokonui.exchanges.base import Exchange as base
from hokonui.exchanges.btce import BTCE as btce


class TestBTCE(TestCase):
    ''' Class for testing BTCE exchange '''

    @classmethod
    @docparams(btce.__name__,"setup")
    def setUp(cls):
        ''' {0}.{1} '''

        print(__name__, ': TestClass.setup_class() ----------')

    @classmethod
    @docparams(btce.__name__,"teardown")
    def tearDown(cls):
        ''' {0}.{1} '''

        print(__name__, ': TestClass.teardown_class() -------')

    @classmethod
    @docparams(btce.__name__,"name")
    def test_name(cls):
        ''' {0}.{1}'''

        ok_(btce.NAME == cls.__name__.replace( 'Test', ''))

    @classmethod
    @docparams(btce.__name__,"price")
    def test_price(cls):
        ''' {0}.{1}'''

        ok_(float(btce.get_current_price()) > 0.00)

    @classmethod
    @unittest.skip("skip while fixing BTC-E url")
    @docparams(btce.__name__,"bid")
    def test_bid(cls):
        ''' {0}.{1}'''

        ok_(float(btce.get_current_bid()) > 0.00)

    @classmethod
    @unittest.skip("skip while fixing BTC-E url")
    @docparams(btce.__name__,"ask")
    def test_ask(cls):
        ''' {0}.{1}'''

        ok_(float(btce.get_current_ask()) > 0.00)

    @classmethod
    @unittest.skip("skip while fixing BTC-E url")
    @docparams(btce.__name__,"bid-lt-ask")
    def test_bid_lt_ask(cls):
        ''' {0}.{1}'''

        bid = float(btce.get_current_bid())
        ask = float(btce.get_current_ask())
        ok_(bid > ask, "bid should be > ask on BTC-E only - Bid : %s Ask %s " % (bid, ask))

    @classmethod
    @unittest.skip("skip while fixing BTC-E url")
    @docparams(btce.__name__,"ticker")
    def test_ticker(cls):
        ''' {0}.{1}'''

        data = json.loads(btce.get_current_ticker())
        bid = float(btce.get_current_bid())
        ask = float(btce.get_current_ask())
        ok_(data["pair"] == base.CCY_DEFAULT, "shd be '%s'" % base.CCY_DEFAULT)
        ok_(ask > 0.00, "ask should not be empty")
        ok_(bid > 0.00, "bid should not be empty")
        ok_(bid > ask, "bid should be > ask - Bid : %s Ask %s " % (bid, ask))
        ok_(float(data["timestamp"]) > 0, "Timestamp should be > zero")

    @classmethod
    @unittest.skip("skip while fixing BTC-E url")
    @docparams(btce.__name__,"orders")
    def test_orders(cls):
        ''' {0}.{1}'''
        orders = btce.get_current_orders()
        ok_(len(orders["asks"]) > 0, "Asks array should not be empty")
        ok_(len(orders["bids"]) > 0, "Bids array should not be empty")
        ok_(orders["source"] == "BTCE", "Source should be 'BTCE'")
        ok_(float(orders["timestamp"]) > 0, "Timestamp should be > zero")

if __name__ == '__main__':
    nose.runmodule()
