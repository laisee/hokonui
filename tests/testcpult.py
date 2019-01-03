''' Module for testing Coinapult exchange '''

from tests import *

libPath = '../hokonui'
if not libPath in sys.path: sys.path.append(libPath)

from hokonui.exchanges.base import Exchange as base
from hokonui.exchanges.coinapult import Coinapult as cplt

class TestCoinapult(TestCase):
    ''' Class for testing Coinapult exchange '''

    @classmethod
    @docparams(cplt.__name__,"name")
    def test_name(cls):
        ''' {0}.{1} '''

        ok_(cplt.NAME == cls.__name__.replace( 'Test', ''))

    @classmethod
    @docparams(cplt.__name__,"price")
    def test_price(cls):
        ''' {0}.{1} '''

        ok_(float(cplt.get_current_price(base.CCY_DEFAULT)) > 0.00)

    @classmethod
    @docparams(cplt.__name__,"bid")
    def test_bid(cls):
        ''' {0}.{1} '''

        ok_(float(cplt.get_current_bid(base.CCY_DEFAULT)) > 0.00)

    @classmethod
    @docparams(cplt.__name__,"ask")
    def test_ask(cls):
        ''' {0}.{1} '''

        ok_(float(cplt.get_current_ask(base.CCY_DEFAULT)) > 0.00)

    @classmethod
    @docparams(cplt.__name__,"bid-lt-ask")
    def test_bid_lt_ask(cls):
        ''' {0}.{1} '''

        bid = float(cplt.get_current_bid(base.CCY_DEFAULT))
        ask = float(cplt.get_current_ask(base.CCY_DEFAULT))
        ok_(bid < ask, "bid should be < ask")

if __name__ == '__main__':
    nose.runmodule()
