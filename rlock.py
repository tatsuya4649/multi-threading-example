#!/bin/env python

import threading
import time

def nest_lock():
	global j
	lock.acquire()
	j = j + 1
	lock.release()

def first_lock():
	global j
	lock.acquire()
	j = j * 2
	nest_lock()
	lock.release()


if __name__ == "__main__":
	# Rlock can lock in nest
	j = 0
	lock = threading.RLock()
	t1 = threading.Thread(target=first_lock)
	t2 = threading.Thread(target=first_lock)
	t1.start()
	t2.start()
