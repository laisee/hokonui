if __package__ is None:
    import sys
    from os import path
    sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
    from hokonui.exchanges.itbit import Itbit as itb
else:
    from ..exchanges.itbit import Itbit as itb

from requests_futures.sessions import FuturesSession

def onResponse():
    print "received response"

session = FuturesSession()

print session.hooks
session.hooks.add(onResponse)

print session.hooks

print "sending ONE "
#print dir(session)
#future_one = session.get('https://btc-e.com/api/3/ticker/btc_usd')

