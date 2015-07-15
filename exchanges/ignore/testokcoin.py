import unittest

class TestOkCoin(unittest.TestCase):

  def test_price(self):
      #print 'Ask   ', okc.get_current_ask()
      self.assertNotEqual(okc.get_current_price(),0.00)

  def test_bid(self):
      #print 'Bid   ', okc.get_current_bid()
      self.assertNotEqual(okc.get_current_bid(),0.00)

  def test_ask(self):
      #print 'Ask   ', okc.get_current_ask()
      self.assertNotEqual(okc.get_current_ask(),0.00)

if __name__ == '__main__':
    if __package__ is None:
        import sys
        from os import path
        sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
        from exchanges.okcoin import OKCoin as okc 
    else:
        from ..exchanges.okcoin import OKCoin as okc 
    unittest.main()
