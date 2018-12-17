''' Module for testing crypto facilities API '''

from tests import *

libPath = '../hokonui'
if not libPath in sys.path: sys.path.append(libPath)

from hokonui.exchanges.base import Exchange as base
from hokonui.exchanges.cryptofac import CryptoFacility as cfc

class TestCryptoFacility(TestCase):
    ''' Class for testing crypto facilities API '''

    SYMBOL = 'fi_xbtusd_180615'

    @classmethod
    def setUp(cls):
        ''' method for test setup '''
        print(__name__, ': TestClass.setup_class() ----------')

    @classmethod
    def tearDown(cls):
        ''' method for test teardown '''
        print(__name__, ': TestClass.teardown_class() -------')

    @classmethod
    def test_name(cls):
        ''' name test method '''
        ok_(cfc.NAME == cls.__name__.replace( 'Test', ''))

    @classmethod
    def test_price(cls):
        ''' method for testing last price '''
        ok_(float(cfc.get_current_price()) > 0.00)

    @classmethod
    def test_bid(cls):
        ''' method for testing bid prices '''
        ok_(float(cfc.get_current_bid()) > 0.00)

    @classmethod
    def test_ask(cls):
        ''' method for testing ask prices '''
        ok_(float(cfc.get_current_ask()) > 0.00)

    @classmethod
    def test_ticker(cls):
        ''' method for testing ticker '''
        data = json.loads(cfc.get_current_ticker())
        ok_(data["pair"] == cfc.CCY_DEFAULT, "shd be '%s'" % cfc.CCY_DEFAULT)
        ok_(float(data["ask"]) > 0.00, "ask shd not be empty")
        ok_(float(data["bid"]) > 0.00, "bid shd not be empty")
        ok_(float(data["bid"]) <= float(data["ask"]), "bid shd be <= ask")
        ok_(float(data["timestamp"]) > 0, "Timestamp should be > zero")

    @classmethod
    def test_orders(cls):
        ''' method for testing orders '''
        orders = cfc.get_current_orders(cls.SYMBOL)
        print(orders)
        #ok_(len(orders["asks"]) > 0, "Asks array shd not be empty")
        #ok_(len(orders["bids"]) > 0, "Bids array shd not be empty")
        ok_(orders["source"] == "CryptoFacility", "Src shd = 'CryptoFacility'")
        ok_(float(orders["timestamp"]) > 0, "Timestamp shd be > zero")

if __name__ == '__main__':
    nose.runmodule()
