''' Module for testing Upbit exchange '''

from tests import *

libPath = '../hokonui'
if not libPath in sys.path: sys.path.append(libPath)

from hokonui.exchanges.base import Exchange as base
from hokonui.exchanges.upbit import Upbit as upb


class TestUpbit(TestCase):
    ''' Class for testing Upbit exchange '''
    @classmethod
    @docparams(upb.__name__, "setup")
    def setUp(cls):
        ''' {0}.{1}'''
        print(__name__, ': TestClass.setup_class() ----------')

    @classmethod
    @docparams(upb.__name__, "teardown")
    def tearDown(cls):
        ''' {0}.{1}'''
        print(__name__, ': TestClass.teardown_class() -------')

    @classmethod
    @docparams(upb.__name__, "name")
    def test_name(cls):
        ''' {0}.{1} '''
        ok_(upb.NAME == cls.__name__.replace('Test', ''))

    @classmethod
    @docparams(upb.__name__, "price")
    def test_price(cls):
        ''' {0}.{1} '''
        ok_(float(upb.get_current_price()) > 0.00)

    @classmethod
    @docparams(upb.__name__, "bid")
    def test_bid(cls):
        ''' {0}.{1} '''
        ok_(float(upb.get_current_bid()) > 0.00)

    @classmethod
    @docparams(upb.__name__, "ask")
    def test_ask(cls):
        ''' {0}.{1} '''
        ok_(float(upb.get_current_ask()) > 0.00)

    @classmethod
    @docparams(upb.__name__, "ticker")
    def test_ticker(cls):
        ''' {0}.{1} '''
        data = json.loads(upb.get_current_ticker())
        ok_(float(data["ask"]) > 0.00, "ask should not be empty")
        ok_(float(data["bid"]) > 0.00, "bid should not be empty")
        ok_(float(data["bid"]) <= float(data["ask"]), "bid should be < ask")
        ok_(float(data["timestamp"]) > 0, "Timestamp should be > zero")

    @classmethod
    @docparams(upb.__name__, "orders")
    def test_orders(cls):
        ''' {0}.{1} '''
        orders = upb.get_current_orders()
        ok_(len(orders["asks"]) > 0, "Asks array should not be empty")
        ok_(len(orders["bids"]) > 0, "Bids array should not be empty")
        ok_(orders["source"] == "Upbit", "Source should be 'Upbit'")
        ok_(float(orders["timestamp"]) > 0, "Timestamp should be > zero")


if __name__ == '__main__':
    nose.runmodule()
