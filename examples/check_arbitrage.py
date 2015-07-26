import thread, time
from decimal import Decimal

if __package__ is None:
    import sys
    from os import path
    sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
    from exchanges.bitfinex import Bitfinex as bfx
    from exchanges.itbit import Itbit as itb
else:
    from ..exchanges.bitfinex import Bitfinex as bfx
    from ..exchanges.itbit import Itbit as itb

SLEEP = 30 # check every 30 seconds
def main():
	"""main function, called at the start of the program"""
 
	def ticker(sleeptime, lock):
		while True:
			lock.acquire()
                        askItBit = itb.get_current_ask('USD')
                        bidItBit = itb.get_current_bid('USD')
                        askBitfinex = bfx.get_current_ask('USD')
                        bidBitfinex = bfx.get_current_bid('USD')
                        print "itBit    : Bid %s Ask %s" % (format(Decimal(bid),'.2f'),format(Decimal(ask),'.2f'))
                        print "Bitfinex : Bid %s Ask %s" % (format(Decimal(bid),'.2f'),format(Decimal(ask),'.2f'))
                        print '-'*20

                        # check for Arb in one direction
                        if askItBit < bidBitfinex: # can we buy for 100 on ItBit and sell for 101 on Bitfinex?
                            arb = bidBitfinex - askItBit 
                            print "Arb #1 exists : ITBIT sell price < Bitfinex buy price "  
                            print "Amount        : %s " % format(Decimal(arb),'.2f')

                        # check for arb in the other direction
                        if bidItBit > askBitfinex: # can we buy for 100 on Bitfinex and sell for 101 on ItBit?
                            arb = askBitfinex - bidItBit 
                            print "Arb #2 exists : Bitfinex sell price < itBit buy price "  
                            print "Amount        : %s " % format(Decimal(arb),'.2f')

                        lock.release()
			time.sleep(sleeptime)

	lock = thread.allocate_lock()
	thread.start_new_thread(ticker, (SLEEP, lock))
 
	while True:
		pass

if __name__ == "__main__":
	main()

