''' Module for testing CoinDesk API '''

from tests import *

libPath = '../hokonui'
if not libPath in sys.path: sys.path.append(libPath)

from hokonui.exchanges.coindesk import CoinDesk as coin


class TestCoinDesk(TestCase):
    ''' Class for testing Coindesk API '''

    @classmethod
    @docparams(coin.__name__,"name")
    def test_name(cls):
        ''' {0}.{1} '''

        ok_(coin.NAME == cls.__name__.replace( 'Test', ''))

    @classmethod
    @docparams(coin.__name__,"price")
    def test_price(cls):
        ''' {0}.{1} '''

        ok_(float(coin.get_current_price()) > 0.00)

    @classmethod
    @docparams(coin.__name__,"past_price")
    def test_past_price(cls):
        ''' {0}.{1} '''

        ok_(float(coin.get_past_price('2015-07-05')) > 0.00)

if __name__ == '__main__':
    nose.runmodule()
