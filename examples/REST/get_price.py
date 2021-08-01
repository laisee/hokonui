if __package__ is None:
    import sys
    from os import path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
    from hokonui.exchanges.bitfinex import Bitfinex as bfx
    from hokonui.exchanges.itbit import Itbit as itb
else:
    from ..hokonui.exchanges.bitfinex import Bitfinex as bfx
    from ..hokonui.exchanges.itbit import Itbit as itb

from decimal import *


def main():
    """main function, called at the start of the program"""

    print('-' * 20)
    bid = bfx.get_current_bid('USD')
    ask = bfx.get_current_ask('USD')
    print("Bitfinex : Bid %s Ask %s" % (format(double(bfx.bid), '.2f'), format(double(bfx.ask), '.2f')))
    print('-' * 20)


if __name__ == "__main__":
    main()
