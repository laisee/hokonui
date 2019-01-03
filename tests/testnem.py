
''' module for testing NEM API '''

from tests import *

libPath = '../hokonui'
if not libPath in sys.path: sys.path.append(libPath)

from hokonui.exchanges.base import Exchange as base
from hokonui.exchanges.nem import Nem as nem

class TestNEM(TestCase):

    ''' Class for testing NEM API '''

    @classmethod
    @docparams(nem.__name__,"setup")
    def setup(cls):
        ''' {0}.{1} '''

        print(__name__, ': TestClass.setup_class() ----------')

    @classmethod
    @docparams(nem.__name__,"teardown")
    def teardown(cls):
        ''' {0}.{1} '''

        print(__name__, ': TestClass.teardown_class() -------')

    @classmethod
    @docparams(nem.__name__,"name")
    def test_name(cls):
        ''' {0}.{1}'''

        ok_(nem.NAME == cls.__name__.replace('Test', ''))

    @classmethod
    @docparams(nem.__name__,"price")
    def test_price(cls):
        ''' {0}.{1}'''

        ok_(float(nem.get_current_price()) > 0.00)

    @classmethod
    @docparams(nem.__name__,"bid")
    def test_bid(cls):
        ''' {0}.{1}'''

        ok_(float(nem.get_current_bid()) > 0.00)

    @classmethod
    @docparams(nem.__name__,"ask")
    def test_ask(cls):
        ''' {0}.{1}'''

        ok_(float(nem.get_current_ask()) > 0.00)

    @classmethod
    @docparams(nem.__name__,"ticker")
    def test_ticker(cls):
        ''' {0}.{1}'''

        data = json.loads(nem.get_current_ticker())
        ok_(data["pair"] == nem.CCY_DEFAULT, "shd be '%s'" % nem.CCY_DEFAULT)
        ok_(float(data["ask"]) > 0.00, "ask should not be empty")
        ok_(float(data["bid"]) > 0.00, "bid should not be empty")
        ok_(float(data["bid"]) <= float(data["ask"]), "bid should be < ask")
        ok_(float(data["timestamp"]) > 0, "Timestamp should be > zero")

    @classmethod
    @docparams(nem.__name__,"orders")
    def test_orders(cls):
        ''' {0}.{1}'''

        orders = nem.get_current_orders()
        ok_(len(orders["asks"]) >= 0, "Asks array should not be empty")
        ok_(len(orders["bids"]) >= 0, "Bids array should not be empty")
        ok_(orders["source"] == "NEM", "Source should be 'NEM'")
        ok_(float(orders["timestamp"]) > 0, "Timestamp should be > zero")

if __name__ == '__main__':
    nose.runmodule()
