
''' module for testing Gemini API '''

from tests import *

libPath = '../hokonui'
if not libPath in sys.path: sys.path.append(libPath)

from hokonui.exchanges.base import Exchange as base
from hokonui.exchanges.gemini import Gemini as q


class TestGemini(TestCase):

    ''' Class for testing Gemini API '''

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
        ok_(q.NAME == cls.__name__.replace( 'Test', ''))

    @classmethod
    def test_price(cls):
        ''' last price test method '''
        ok_(float(q.get_current_price(q.CCY_DEFAULT)) > 0.00)

    @classmethod
    def test_bid(cls):
        ''' bid price test method '''
        ok_(float(q.get_current_bid(q.CCY_DEFAULT)) > 0.00)

    @classmethod
    def test_ask(cls):
        ''' ask price test method '''
        ok_(float(q.get_current_ask(q.CCY_DEFAULT)) > 0.00)

    @classmethod
    def test_ticker(cls):
        ''' ticker test method '''

        data = json.loads(q.get_current_ticker(q.CCY_DEFAULT))
        ok_(data["pair"] == q.CCY_DEFAULT, "shd be '%s'" % q.CCY_DEFAULT)
        ok_(float(data["ask"]) > 0.00, "ask should not be empty")
        ok_(float(data["bid"]) > 0.00, "bid should not be empty")
        ok_(float(data["bid"]) <= float(data["ask"]), "bid should be < ask")
        ok_(float(data["timestamp"]) > 0, "Timestamp should be > zero")

    @classmethod
    def test_orders(cls):
        ''' orders test method '''
        orders = q.get_current_orders(q.CCY_DEFAULT)
        ok_(len(orders["asks"]) > 0, "Asks array should not be empty")
        ok_(len(orders["bids"]) > 0, "Bids array should not be empty")
        ok_(orders["source"] == "Gemini", "Source should be 'Gemini'")
        ok_(float(orders["timestamp"]) > 0, "Timestamp should be > zero")


if __name__ == '__main__':
    nose.runmodule()
