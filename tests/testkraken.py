''' Module for testing Kraken API '''

from tests import *

libPath = '../hokonui'
if not libPath in sys.path: sys.path.append(libPath)

from hokonui.exchanges.base import Exchange as base
from hokonui.exchanges.kraken import Kraken as kraken


class TestKraken(TestCase):
    ''' Class for testing Kraken API '''

    @classmethod
    def setUp(cls):
        ''' Method for test setup '''
        print(__name__, ': TestClass.setup_class() ----------')

    @classmethod
    def tearDown(cls):
        ''' Method for test teardown '''
        print(__name__, ': TestClass.teardown_class() -------')

    @classmethod
    def test_name(cls):
        ''' Method for testing name '''
        ok_(kraken.NAME == cls.__name__.replace( 'Test', ''))

    @classmethod
    def test_price(cls):
        ''' Method for testing last price '''
        body = '{"pair":"XXBTZUSD"}'
        ok_(float(kraken.get_current_price(None, None, body)) > 0.00)

    @classmethod
    def test_bid(cls):
        ''' Method for testing bid price '''
        body = '{"pair":"XXBTZJPY"}'
        ok_(float(kraken.get_current_bid(None, None, body)) > 0.00)

    @classmethod
    def test_ask(cls):
        ''' Method for testing ask price '''
        body = '{"pair":"XXBTZJPY"}'
        ok_(float(kraken.get_current_ask(None, None, body)) > 0.00)

    @classmethod
    def test_ticker(cls):
        ''' Method for testing ticker '''
        body = '{"pair":"XXBTZJPY"}'
        data = json.loads(kraken.get_current_ticker(None, None, body))
        ok_(data["pair"] == 'XXBTZJPY', "pair should be 'XXBTZJPY'")
        ok_(float(data["ask"]) > 0.00, "ask should not be empty")
        ok_(float(data["bid"]) > 0.00, "bid should not be empty")
        ok_(float(data["bid"]) <= float(data["ask"]), "bid should be <= ask")
        ok_(float(data["timestamp"]) > 0, "Timestamp should be > zero")

    @classmethod
    def test_orders(cls):
        ''' Method for testing orders '''
        body = '{"pair":"XXBTZJPY", "count":"10"}'
        orders = kraken.get_current_orders(None, None, body, 25)
        ok_(len(orders["asks"]) > 0, "Asks array should not be empty")
        ok_(len(orders["bids"]) > 0, "Bids array should not be empty")
        ok_(orders["source"] == "Kraken", "Source should be 'Kraken'")
        ok_(float(orders["timestamp"]) > 0, "Timestamp should be > zero")

if __name__ == '__main__':
    nose.runmodule()
