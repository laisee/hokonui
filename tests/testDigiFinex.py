''' Module for testing Digitfinex exchange '''

from tests import *

libPath = '../hokonui'
if not libPath in sys.path: sys.path.append(libPath)

from hokonui.exchanges.base import Exchange as base
from hokonui.exchanges.digifinex import Digifinex as dfx


class TestDigitfinex(TestCase):
    ''' Class for testing Digitfinex exchange '''

    @classmethod
    @docparams(dfx.__name__,"setup")
    def setUp(cls):
        ''' {0}.{1}'''
        print(__name__, ': TestClass.setup_class() ----------')

    @classmethod
    @docparams(dfx.__name__,"teardown")
    def tearDown(cls):
        ''' {0}.{1}'''
        print(__name__, ': TestClass.teardown_class() -------')

    @classmethod
    @docparams(dfx.__name__,"name")
    @unittest.skip("skip while creating Digitfinex API calls ")
    def test_name(cls):
        ''' {0}.{1} '''
        ok_(dfx.NAME == cls.__name__.replace( 'Test', ''))

    @classmethod
    @docparams(dfx.__name__,"price")
    @unittest.skip("skip while creating Digitfinex API calls ")
    def test_price(cls):
        ''' {0}.{1} '''
        ok_(float(dfx.get_current_price(dfx.CCY_DEFAULT)) > 0.00)

    @classmethod
    @docparams(dfx.__name__,"bid")
    @unittest.skip("skip while creating Digitfinex API calls ")
    def test_bid(cls):
        ''' {0}.{1} '''
        ok_(float(dfx.get_current_bid(dfx.CCY_DEFAULT)) > 0.00)

    @classmethod
    @docparams(dfx.__name__,"ask")
    @unittest.skip("skip while creating Digitfinex API calls ")
    def test_ask(cls):
        ''' {0}.{1} '''
        ok_(float(dfx.get_current_ask(dfx.CCY_DEFAULT)) > 0.00)

    @classmethod
    @docparams(dfx.__name__,"ticker")
    @unittest.skip("skip while creating Digitfinex API calls ")
    def test_ticker(cls):
        ''' {0}.{1} '''
        data = json.loads(dfx.get_current_ticker(dfx.CCY_DEFAULT))
        ok_(data["pair"] == dfx.CCY_DEFAULT, "shd be '%s'" % dfx.CCY_DEFAULT)
        ok_(float(data["ask"]) > 0.00, "ask should not be empty")
        ok_(float(data["bid"]) > 0.00, "bid should not be empty")
        ok_(float(data["bid"]) <= float(data["ask"]), "bid should be < ask")
        ok_(float(data["timestamp"]) > 0, "Timestamp should be > zero")

    @classmethod
    @docparams(dfx.__name__,"orders")
    @unittest.skip("skip while creating Digitfinex API calls ")
    def test_orders(cls):
        ''' {0}.{1} '''
        orders = dfx.get_current_orders(dfx.CCY_DEFAULT)
        ok_(len(orders["asks"]) > 0, "Asks array should not be empty")
        ok_(len(orders["bids"]) > 0, "Bids array should not be empty")
        ok_(orders["source"] == "Digitfinex", "Source should be 'Digitfinex'")
        ok_(float(orders["timestamp"]) > 0, "Timestamp should be > zero")

if __name__ == '__main__':
    nose.runmodule()
