if __package__ is None:
    import sys
    from os import path
    sys.path.append(
        path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))
    from hokonui.exchanges.itbit import Itbit as itb
else:
    from ..hokonui.exchanges.itbit import Itbit as itb

from requests_futures.sessions import FuturesSession

print "getting price for ItBit exchange "
session = FuturesSession()
future_one = session.get(itb.TICKER_URL)
