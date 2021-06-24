#!/bin/env python

import threading
import time
import sys

def exth(i):
	time.sleep(1)
	print(i)

if __name__ == "__main__":
	for i in range(4):
		t = threading.Thread(target=exth,args=(i,))
		t.setDaemon(True)
		t.start()
	# if exist only 'daemon thread', finish program
	sys.exit(0)
	# not exec
	print(threading.active_count())
