import time
from decimal import Decimal

try:
    import thread
except ImportError:
    import _thread as thread

if __package__ is None:
    import sys
    from os import path
    sys.path.append(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))
    # import Bitfinex library
    from hokonui.exchanges.bitfinex import Bitfinex as bfx
    # import ITBIT library
    from hokonui.exchanges.itbit import Itbit as itb
else:
    # import ITBIT library
    # import Bitfinex library
    from ..hokonui.exchanges.bitfinex import Bitfinex as bfx
    from ..hokonui.exchanges.itbit import Itbit as itb

SLEEP = 30  # check every 30 seconds


def main():
    """main function, called at the start of the program"""
    def ticker(sleeptime, lock):
        while True:
            lock.acquire()
            ask_itbit = format(Decimal(itb.get_current_ask('USD'), '.2f'))
            bid_itbit = format(Decimal(itb.get_current_bid('USD'), '.2f'))
            ask_bitfinex = format(Decimal(bfx.get_current_ask('USD', '.2f')))
            bid_bitfinex = format(Decimal(bfx.get_current_bid('USD', '.2f')))
            print("It : Bid %s Ask %s" % (bid_itbit, ask_itbit))
            print("Bfx: Bid %s Ask %s" % (bid_bitfinex, ask_bitfinex))
            print('-' * 20)

            # check for Arb in one direction (buy @ ItBit, sell @ Bitfinex)
            if ask_itbit < bid_bitfinex:
                arb = bid_bitfinex - ask_itbit
                print("Arb #1 exists : ITBIT sell price < Bitfinex buy price ")
                print("Amount        : %s " % format(Decimal(arb), '.2f'))

            # check for arb in the other direction (buy @ Bitfinex, sell @ ItBit)
            if bid_itbit > ask_bitfinex:
                arb = ask_bitfinex - bid_itbit
                print("Arb #2 exists : Bitfinex sell price < itBit buy price ")
                print("Amount        : %s " % format(Decimal(arb), '.2f'))

            lock.release()
            time.sleep(sleeptime)

    lock = thread.allocate_lock()
    thread.start_new_thread(ticker, (SLEEP, lock))


while True:
    pass

if __name__ == "__main__":
    main()
