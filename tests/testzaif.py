''' module for testing Zaif API '''

from tests import *

libPath = '../hokonui'
if not libPath in sys.path: sys.path.append(libPath)

from hokonui.exchanges.base import Exchange as base
from hokonui.exchanges.zaif import Zaif as zf


class TestZaif(TestCase):

    ''' Class for testing Zaif API '''

    @classmethod
    def setup(cls):
        ''' setup method '''
        print(__name__, ': TestClass.setup_class() ----------')

    @classmethod
    def teardown(cls):
        ''' test teardown method '''
        print(__name__, ': TestClass.teardown_class() -------')

    @classmethod
    def test_name(cls):
        ''' name test method '''
        ok_(zf.NAME == cls.__name__.replace('Test', ''))

    @classmethod
    def test_price(cls):
        ''' last price test method '''
        ok_(float(zf.get_current_price(zf.CCY_DEFAULT)) > 0.00)

    @classmethod
    def test_bid(cls):
        ''' bid price test method '''
        ok_(float(zf.get_current_bid(zf.CCY_DEFAULT)) > 0.00)

    @classmethod
    def test_ask(cls):
        ''' ask price test method '''
        ok_(float(zf.get_current_ask(zf.CCY_DEFAULT)) > 0.00)

    @classmethod
    def test_ticker(cls):
        ''' ticket test method '''

        data = json.loads(zf.get_current_ticker(zf.CCY_DEFAULT))
        ok_(data["pair"] == zf.CCY_DEFAULT, "shd be '%s'" % zf.CCY_DEFAULT)
        ok_(float(data["ask"]) > 0.00, "ask should not be empty")
        ok_(float(data["bid"]) > 0.00, "bid should not be empty")
        ok_(float(data["bid"]) <= float(data["ask"]), "bid should be < ask")
        ok_(float(data["timestamp"]) > 0, "Timestamp should be > zero")

    @classmethod
    def test_orders(cls):
        ''' orders test method '''
        orders = zf.get_current_orders(zf.CCY_DEFAULT)
        ok_(len(orders["asks"]) > 0, "Asks array should not be empty")
        ok_(len(orders["bids"]) > 0, "Bids array should not be empty")
        ok_(orders["source"] == "Zaif", "Source should be 'Zaif'")
        ok_(float(orders["timestamp"]) > 0, "Timestamp should be > zero")

if __name__ == '__main__':
    nose.runmodule()
