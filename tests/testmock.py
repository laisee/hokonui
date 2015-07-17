import string
import nose
from nose.tools import ok_
from unittest import TestCase

if __package__ is None:
    import sys
    from os import path
    sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
    from exchanges.mock import MockExchange as mock
else:
    from ..exchanges.mock import MockExchange as mock

class TestMockExchange(TestCase):

  def setUp(self):
      print(__name__, ': TestClass.setup_class() ----------')

  def tearDown(self):
      print(__name__, ': TestClass.teardown_class() -------')

  def test_name(self):
      ok_(mock.NAME==string.replace(type(self).__name__,'Test',''))

if __name__ == '__main__':
    nosetest.runmodule()
