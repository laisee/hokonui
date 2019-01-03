''' Module for testing Mock Exchange '''

from tests import *

libPath = '../hokonui'
if not libPath in sys.path: sys.path.append(libPath)

from hokonui.exchanges.base import Exchange as base
from hokonui.exchanges.mock import MockExchange as mock


class TestMockExchange(TestCase):
    ''' Class for testing Mock Exchange '''

    @classmethod
    @docparams(mock.__name__,"setup")
    def setUp(cls):
        ''' {0}.{1} '''

        print(__name__, ': TestClass.setup_class() ----------')

    @classmethod
    @docparams(mock.__name__,"teardown")
    def tearDown(cls):
        ''' {0}.{1} '''

        print(__name__, ': TestClass.teardown_class() -------')

    @classmethod
    @docparams(mock.__name__,"name")
    def test_name(cls):
        ''' {0}.{1} '''

        ok_(mock.NAME == cls.__name__.replace( 'Test', ''))

    @classmethod
    @unittest.skip("skip while building mock service")
    @docparams(mock.__name__,"ask")
    def test_ask(cls):
        ''' {0}.{1} '''

        with assert_raises(ValueError) as cme:
            mock.get_current_ask(base.CCY_DEFAULT)
        ex = cme.exception
        ok_(ex.message == "Not implemented yet")

    @classmethod
    @unittest.skip("skip while building mock service")
    @docparams(mock.__name__,"bid")
    def test_bid(cls):
        ''' {0}.{1} '''

        with assert_raises(ValueError) as cme:
            mock.get_current_bid(base.CCY_DEFAULT)
        ex = cme.exception
        ok_(ex.message == "Not implemented yet")

    @classmethod
    @unittest.skip("skip while building mock service")
    @docparams(mock.__name__,"orders")
    def test_orders(cls):
        ''' {0}.{1} '''

        with assert_raises(ValueError) as cme:
            mock.get_current_orders(base.CCY_DEFAULT)
        ex = cme.exception
        ok_(ex.message == "Not implemented yet")

if __name__ == '__main__':
    nose.runmodule()
