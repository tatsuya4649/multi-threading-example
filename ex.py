#!/bin/env python3
import threading
import time

# this is worker1 function
def worker1(sec):
	time.sleep(sec)
	print("worker1 => %d"%time.time())

# this is worker2 function
def worker2(sec):
	time.sleep(sec)
	print("worker2 => %d"%time.time())


if __name__ == "__main__":
	t1 = threading.Thread(target=worker1,args=(2,))
	t2 = threading.Thread(target=worker2,args=(5,))
	
	# start multithread
	t1.start()
	t2.start()

	print("Hello")
	# wait for ending 't1'
	t1.join()
	print("World")

	# will end 't2'
