#!/bin/env python

import threading
import time

def ex_notlock():
	global k
	for _ in range(100):
		k+=1

def ex_lock():
	global j
	global lock
	lock.acquire()
	for _ in range(100):
		j+=1
	lock.release()

if __name__ == "__main__":
	j = 0
	lock = threading.Lock()
	t1 = threading.Thread(target=ex_lock,args=())
	t2 = threading.Thread(target=ex_lock,args=())
	t1.start()
	t2.start()
	print(j)
	"""
		not race condition!!!
		Python use GIL (Global Interpreter Lock) 
	"""
	k = 0
	t1 = threading.Thread(target=ex_notlock,args=())
	t2 = threading.Thread(target=ex_notlock,args=())
	t1.start()
	t2.start()
	print(k)
