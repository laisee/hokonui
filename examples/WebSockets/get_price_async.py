from requests_futures.sessions import FuturesSession
if __package__ is None:
    import sys
    from os import path
    sys.path.append(
        path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))
    from hokonui.exchanges.itbit import Itbit as itb
else:
    from ..hokonui.exchanges.itbit import Itbit as itb


def on_response(url: str):
    ''' response handler '''
    print("Got a response for URL ", url)

print("Getting price from ItBit exchange ")
session = FuturesSession()
print(dir(session))
session.hooks["response"] = on_response

func = session.hooks["response"]
func(itb.TICKER_URL)
future_one = session.get(itb.TICKER_URL)
print("Finished getting price from ItBit exchange ")
