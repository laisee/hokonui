''' Module for testing Bitcoinaverage API '''

from tests import *

libPath = '../hokonui'
if not libPath in sys.path: sys.path.append(libPath)

from hokonui.exchanges.base import Exchange as base
from hokonui.exchanges.bitcoinavg import BitcoinAverage as avg


class TestBitcoinAverage(TestCase):
    ''' Class for executing Bitcoinaverage API test '''

    @classmethod
    @docparams(avg.__name__,"setup")
    def setup(cls):
        ''' {0}.{1} '''
        print(__name__, ': TestClass.setup_class() ----------')

    @classmethod
    @docparams(avg.__name__,"teardown")
    def teardown(cls):
        ''' {0}.{1} '''
        print(__name__, ': TestClass.teardown_class() -------')

    @classmethod
    @docparams(avg.__name__,"name")
    def test_name(cls):
        ''' {0}.{1} '''

        ok_(avg.NAME == cls.__name__.replace( 'Test', ''))

    @classmethod
    @docparams(avg.__name__,"price")
    def test_price(cls):
        ''' {0}.{1} '''

        ok_(float(avg.get_current_price(base.CCY_DEFAULT)) > 0.00)

    @classmethod
    @docparams(avg.__name__,"bid")
    def test_bid(cls):
        ''' {0}.{1} '''

        ok_(float(avg.get_current_bid(base.CCY_DEFAULT)) > 0.00)

    @classmethod
    @docparams(avg.__name__,"ask")
    def test_ask(cls):
        ''' {0}.{1} '''

        ok_(float(avg.get_current_ask(base.CCY_DEFAULT)) > 0.00)

    @classmethod
    @docparams(avg.__name__,"ticker")
    def test_ticker(cls):
        ''' {0}.{1} '''

        data = json.loads(avg.get_current_ticker(base.CCY_DEFAULT))
        ok_(data["pair"] == base.CCY_DEFAULT, "shd be '%s'" % base.CCY_DEFAULT)
        ok_(float(data["ask"]) > 0.00, "ask should not be empty")
        ok_(float(data["bid"]) > 0.00, "bid should not be empty")
        ok_(float(data["bid"]) <= float(data["ask"]), "bid should be < ask")
        ok_(float(data["timestamp"]) > 0, "Timestamp should be > zero")

    @classmethod
    @unittest.skip("skip while reviewing BTC AvgAPI ")
    @docparams(avg.__name__,"volumes")
    def test_volume(cls):
        ''' {0}.{1} '''
        vol = avg.get_current_volume(base.CCY_DEFAULT)
        ok_(float(vol["quantity"]) >= 0, "quantity shd be valid number >= 0")
        ok_(vol["source"] == "BitcoinAverage", "Source should be 'BitcoinAverage'")
        ok_(float(vol["timestamp"]) > 0, "Timestamp should be greater than zero")

if __name__ == '__main__':
    nose.runmodule()
