''' Module for testing Bitstamp exchange '''

from tests import *

libPath = '../hokonui'
if not libPath in sys.path: sys.path.append(libPath)

from hokonui.exchanges.base import Exchange as base
from hokonui.exchanges.bitstamp import Bitstamp as bts


class TestBitstamp(TestCase):
    ''' Class for testing Bitstamp exchange '''

    @classmethod
    def setUp(cls):
        ''' Method for testing setup '''
        print(__name__, ': TestClass.setup_class() ----------')

    @classmethod
    def tearDown(cls):
        ''' Method for testing teardown '''
        print(__name__, ': TestClass.teardown_class() -------')

    @classmethod
    def test_name(cls):
        ''' Method for testing name '''
        ok_(bts.NAME == cls.__name__.replace( 'Test', ''))

    @classmethod
    def test_price(cls):
        ''' Method for testing last price '''
        ok_(float(bts.get_current_price(bts.CCY_DEFAULT)) > 0.00)

    @classmethod
    def test_bid(cls):
        ''' Method for testing bid prices '''
        ok_(float(bts.get_current_bid(bts.CCY_DEFAULT)) > 0.00)

    @classmethod
    def test_ask(cls):
        ''' Method for testing ask prices '''
        ok_(float(bts.get_current_ask(bts.CCY_DEFAULT)) > 0.00)

    @classmethod
    def test_ticker(cls):
        ''' Method for testing ticker '''
        data = json.loads(bts.get_current_ticker(bts.CCY_DEFAULT))
        ok_(data["pair"] == bts.CCY_DEFAULT, "shd be '%s'" % bts.CCY_DEFAULT)
        ok_(float(data["ask"]) > 0.00, "ask should not be empty")
        ok_(float(data["bid"]) > 0.00, "bid should not be empty")
        ok_(float(data["bid"]) <= float(data["ask"]), "bid should be < ask")
        ok_(float(data["timestamp"]) > 0, "Timestamp should be > zero")

    @classmethod
    def test_orders(cls):
        ''' Method for testing orders '''
        orders = bts.get_current_orders(bts.CCY_DEFAULT)
        ok_(len(orders["asks"]) > 0, "Asks array should not be empty")
        ok_(len(orders["bids"]) > 0, "Bids array should not be empty")
        ok_(orders["source"] == "Bitstamp", "Source should be 'Bitstamp'")
        ok_(float(orders["timestamp"]) > 0, "Timestamp should be > zero")



if __name__ == '__main__':
    nose.runmodule()
