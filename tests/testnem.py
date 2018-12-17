
''' module for testing NEM API '''

from tests import *

libPath = '../hokonui'
if not libPath in sys.path: sys.path.append(libPath)

from hokonui.exchanges.base import Exchange as base
from hokonui.exchanges.nem import Nem as nem

class TestNEM(TestCase):

    ''' Class for testing NEM API '''

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
        ok_(nem.NAME == cls.__name__.replace('Test', ''))

    @classmethod
    def test_price(cls):
        ''' last price test method '''
        ok_(float(nem.get_current_price()) > 0.00)

    @classmethod
    def test_bid(cls):
        ''' bid price test method '''
        ok_(float(nem.get_current_bid()) > 0.00)

    @classmethod
    def test_ask(cls):
        ''' ask price test method '''
        ok_(float(nem.get_current_ask()) > 0.00)

    @classmethod
    def test_ticker(cls):
        ''' ticket test method '''

        data = json.loads(nem.get_current_ticker())
        ok_(data["pair"] == nem.CCY_DEFAULT, "shd be '%s'" % nem.CCY_DEFAULT)
        ok_(float(data["ask"]) > 0.00, "ask should not be empty")
        ok_(float(data["bid"]) > 0.00, "bid should not be empty")
        ok_(float(data["bid"]) <= float(data["ask"]), "bid should be < ask")
        ok_(float(data["timestamp"]) > 0, "Timestamp should be > zero")

    @classmethod
    def test_orders(cls):
        ''' orders test method '''
        orders = nem.get_current_orders()
        ok_(len(orders["asks"]) >= 0, "Asks array should not be empty")
        ok_(len(orders["bids"]) >= 0, "Bids array should not be empty")
        ok_(orders["source"] == "NEM", "Source should be 'NEM'")
        ok_(float(orders["timestamp"]) > 0, "Timestamp should be > zero")

if __name__ == '__main__':
    nose.runmodule()
