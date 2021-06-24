#!/bin/env python

import threading
import time

event = threading.Event()
event.clear()
i = 0

def event_go():
	global i
	while True:
		if i < 5:
			i = i + 1
		elif i < 10:
	# wake up thread that waiting for 'set'
			i = i + 1
			event.set()
		else:
			i = 0
			event.clear()
		print(i)
		time.sleep(2)

def event_wait():
	while True:
		if (event.is_set()):
			print("Go!!!")
		else:
			print("Wait...")
			event.wait()
		time.sleep(1)

t1 = threading.Thread(target=event_wait)
t1.start()
t2 = threading.Thread(target=event_go)
t2.start()
