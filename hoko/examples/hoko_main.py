import thread, time
from decimal import Decimal

if __package__ is None:
    import sys
    from os import path
    sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
    from exchanges.itbit import Itbit as itb
else:
    from ..exchanges.itbit import Itbit as itb

def main():
	"""main function, called at the start of the program"""
 
	def ticker(sleeptime, lock):
		lastask = 0
		lastbid = 0
		while True:
			lock.acquire()
                        ask = itb.get_current_ask('USD')
                        bid = itb.get_current_bid('USD')
                        print "Bid %s Ask %s" % (format(Decimal(bid),'.2f'),format(Decimal(ask),'.2f'))
                        print '-'*20
                        lock.release()
			time.sleep(sleeptime)

	lock = thread.allocate_lock()
	thread.start_new_thread(ticker, (10, lock))
 
	while True:
		pass

if __name__ == "__main__":
	main()

