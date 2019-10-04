''' Module for testing Coinhako exchange '''

from tests import *

libPath = '../hokonui'
if not libPath in sys.path: sys.path.append(libPath)

from hokonui.exchanges.base import Exchange as base
from hokonui.exchanges.coinhako import Coinhako as chk


class TestCoinhako(TestCase):
    ''' Class for testing Coinhako exchange '''

    @docparams(chk.__name__,"setup")
    def setUp(cls):
        ''' {0}.{1}'''

        print(__name__, ': TestClass.setup_class() ----------')

    @docparams(chk.__name__,"teardown")
    def tearDown(cls):
        ''' {0}.{1}'''

        print(__name__, ': TestClass.teardown_class() -------')

    @classmethod
    @docparams(chk.__name__,"name")
    def test_name(cls):
        ''' {0}.{1} '''

        ok_(chk.NAME == cls.__name__.replace( 'Test', ''), "Name should be '%s', was '%s'" % (chk.NAME, cls.__name__))

    @docparams(chk.__name__,"price")
    def test_price(cls):
        ''' {0}.{1} '''

        ok_(float(chk.get_current_price(chk.CCY_DEFAULT)) > 0.00)

    @docparams(chk.__name__,"bid")
    def test_bid(cls):
        ''' {0}.{1} '''

        ok_(float(chk.get_current_bid(chk.CCY_DEFAULT)) > 0.00)

    @docparams(chk.__name__,"ask")
    def test_ask(cls):
        ''' {0}.{1} '''

        ok_(float(chk.get_current_ask(chk.CCY_DEFAULT)) > 0.00)

    @docparams(chk.__name__,"ticker")
    def test_ticker(cls):
        ''' {0}.{1} '''

        data = json.loads(chk.get_current_ticker(chk.CCY_DEFAULT))
        ok_(data["pair"] == chk.CCY_DEFAULT, "shd be '%s'" % chk.CCY_DEFAULT)
        ok_(float(data["ask"]) > 0.00, "ask should not be empty")
        ok_(float(data["bid"]) > 0.00, "bid should not be empty")
        ok_(float(data["bid"]) != float(data["ask"]), "bid [%s]should be < ask [%s]" % (data["bid"],data["ask"]))
        ok_(float(data["timestamp"]) > 0, "Timestamp should be > zero")

    @docparams(chk.__name__,"orders")
    @unittest.skip("orders API not available for Coinhako")
    def test_orders(cls):
        ''' {0}.{1} '''

        orders = chk.get_current_orders(chk.CCY_DEFAULT)
        ok_(len(orders["asks"]) > 0, "Asks array should not be empty")
        ok_(len(orders["bids"]) > 0, "Bids array should not be empty")
        ok_(orders["source"] == "Coinhako", "Source should be 'Coinhako'")
        ok_(float(orders["timestamp"]) > 0, "Timestamp should be > zero")

if __name__ == '__main__':
    nose.runmodule()
