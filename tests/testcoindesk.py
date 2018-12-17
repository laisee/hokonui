''' Module for testing CoinDesk API '''

from tests import *

libPath = '../hokonui'
if not libPath in sys.path: sys.path.append(libPath)

from hokonui.exchanges.coindesk import CoinDesk as coin


class TestCoinDesk(TestCase):
    ''' Class for testing Coindesk API '''

    @classmethod
    def test_name(cls):
        ''' Method for tesing name '''
        ok_(coin.NAME == cls.__name__.replace( 'Test', ''))

    @classmethod
    def test_price(cls):
        ''' Method for tesing current price '''
        ok_(float(coin.get_current_price()) > 0.00)

    @classmethod
    def test_past_price(cls):
        ''' Method for tesing past price '''
        ok_(float(coin.get_past_price('2015-07-05')) > 0.00)

if __name__ == '__main__':
    nose.runmodule()
