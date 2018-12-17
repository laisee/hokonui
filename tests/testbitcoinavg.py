''' MOdule for testing Bitcoinaverage API '''

from test import *

libPath = '../hokonui'
if not libPath in sys.path: sys.path.append(libPath)

from hokonui.exchanges.base import Exchange as base
from hokonui.exchanges.bitcoinavg import BitcoinAverage as avg


class TestBitcoinAverage(TestCase):
    ''' Class for executing Bitcoinaverage API test '''

    @classmethod
    def setup(cls):
        ''' setup method '''
        print(__name__, ': TestClass.setup_class() ----------')

    @classmethod
    def teardown(cls):
        ''' teardown method '''
        print(__name__, ': TestClass.teardown_class() -------')

    @classmethod
    @unittest.skip("skip while API volume call is rebuilt")
    def test_name(cls):
        ''' method for testing name '''
        ok_(avg.NAME == cls.__name__.replace( 'Test', ''))

    @classmethod
    @unittest.skip("skip while API volume call is rebuilt")
    def test_price(cls):
        ''' method for testing last price '''
        ok_(avg.get_current_price(base.CCY_DEFAULT) > 0.00)

    @classmethod
    @unittest.skip("skip while API volume call is rebuilt")
    def test_bid(cls):
        ''' method for testing bid price '''
        ok_(avg.get_current_bid(base.CCY_DEFAULT) > 0.00)

    @classmethod
    @unittest.skip("skip while API volume call is rebuilt")
    def test_ask(cls):
        ''' method for testing ask price '''
        ok_(avg.get_current_ask(base.CCY_DEFAULT) > 0.00)

    @classmethod
    @unittest.skip("skip while API volume call is rebuilt")
    def test_ticker(cls):
        ''' method for testing ticker '''
        data = json.loads(avg.get_current_ticker(base.CCY_DEFAULT))
        ok_(data["pair"] == base.CCY_DEFAULT, "shd be '%s'" % base.CCY_DEFAULT)
        ok_(data["ask"] > 0.00, "ask should not be empty")
        ok_(data["bid"] > 0.00, "bid should not be empty")
        ok_(data["bid"] <= data["ask"], "bid should be < ask")
        ok_(float(data["timestamp"]) > 0, "Timestamp should be > zero")

    @classmethod
    @unittest.skip("skip while API volume call is rebuilt")
    def test_volume(cls):
        ''' method for testing volumes '''
        vol = avg.get_current_volume(base.CCY_DEFAULT)
        ok_(float(vol["quantity"]) >= 0, "quantity shd be valid number >= 0")
        ok_(vol["source"] == "BitcoinAverage", "Source should be 'BitcoinAverage'")
        ok_(float(vol["timestamp"]) > 0, "Timestamp should be greater than zero")

if __name__ == '__main__':
    nose.runmodule()
