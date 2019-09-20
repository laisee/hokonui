
''' module for testing Quoine API '''

from tests import *

libPath = '../hokonui'
if not libPath in sys.path: sys.path.append(libPath)

from hokonui.exchanges.base import Exchange as base
from hokonui.exchanges.quoine import Quoine as q

class TestQuoine(TestCase):

    ''' Class for testing Quoine API '''

    @classmethod
    @docparams(q.__name__,'setup')
    def setup(cls):
        ''' {0}.{1} '''

        print(__name__, ': TestClass.setup_class() ----------')

    @classmethod
    @docparams(q.__name__,'teardown')
    def teardown(cls):
        ''' {0}.{1} '''

        print(__name__, ': TestClass.teardown_class() -------')

    @classmethod
    @docparams(q.__name__,'name')
    def test_name(cls):
        ''' {0}.{1} ''' 

        ok_(q.NAME == cls.__name__.replace( 'Test', ''))

    @classmethod
    @docparams(q.__name__,'price')
    def test_price(cls):
        ''' {0}.{1} ''' 

        ok_(float(q.get_current_price(base.CCY_DEFAULT)) > 0.00)

    @classmethod
    @docparams(q.__name__,'bid')
    def test_bid(cls):
        ''' {0}.{1} ''' 

        ok_(float(q.get_current_bid(base.CCY_DEFAULT)) > 0.00)

    @classmethod
    @docparams(q.__name__,'ask')
    def test_ask(cls):
        ''' {0}.{1} ''' 

        ok_(float(q.get_current_ask(base.CCY_DEFAULT)) > 0.00)

    @classmethod
    @docparams(q.__name__,'ticker')
    def test_ticker(cls):
        ''' {0}.{1} ''' 

        data = json.loads(q.get_current_ticker(base.CCY_DEFAULT))
        ok_(data["pair"] == base.CCY_DEFAULT, "shd be '%s'" % base.CCY_DEFAULT)
        ok_(float(data["ask"]) > 0.00, "ask should not be empty")
        ok_(float(data["bid"]) > 0.00, "bid should not be empty")
        ok_(float(data["bid"]) <= float(data["ask"]), "bid should be < ask")
        ok_(float(data["timestamp"]) > 0, "Timestamp should be > zero")

    @classmethod
    @docparams(q.__name__,'orders')
    def test_orders(cls):
        ''' {0}.{1} ''' 

        ccy_id = cls.CcyToId(base.CCY_DEFAULT)
        orders = q.get_current_orders(ccy_id)
        ok_(len(orders["asks"]) > 0, "Asks array should not be empty")
        ok_(len(orders["bids"]) > 0, "Bids array should not be empty")
        ok_(orders["source"] == "Quoine", "Source should be 'Quoine'")
        ok_(float(orders["timestamp"]) > 0, "Timestamp should be > zero")

    @staticmethod
    def CcyToId(ccy):
        ''' static method for converting CCY string to ID value '''

        ccyid = -1
        if ccy == 'USD':
            ccyid = 1
        elif ccy == 'EUR':
            ccyid = 3
        elif ccy == 'JPY':
            ccyid = 5
        elif ccy == 'SGD':
            ccyid = 7
        elif ccy == 'HKD':
            ccyid = 9
        elif ccy == 'IDR':
            ccyid = 11
        elif ccy == 'AUD':
            ccyid = 13
        elif ccy == 'PHP':
            ccyid = 15
        elif ccy == 'CNY':
            ccyid = 17
        elif ccy == 'INR':
            ccyid = 18
        else:
            raise ValueError("Invalid Currency : %s " % ccy)
        return ccyid


if __name__ == '__main__':
    nose.runmodule()
