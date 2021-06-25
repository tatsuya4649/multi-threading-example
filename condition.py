#!/bin/env python

import threading
import collections
import time
import random
import math


class Consume(threading.Thread):
	def __init__(self,number):
		super().__init__()
		self.number = number
	def run(self):
		global stack
		global cd
		while True:
			cd.acquire()
			cd.wait_for(stack_count,timeout=None)
			element = stack.pop()
			print(f"Consume {self.number} -> {element}")
			cd.release()
			sleep()

class Produce(threading.Thread):
	def run(self):
		global stack
		global cd
		while True:
			cd.acquire()
			element = rand()
			stack.append(element)
			print(f"Produce -> {element}")
			cd.notify()
			cd.release()
			sleep()

_SLEEP_TIME = 0.5
def sleep():
	time.sleep(_SLEEP_TIME)

def rand():
	return math.floor((random.random()*10000)%100)

def stack_count():
	return len(stack)

if __name__ == "__main__":
	# LIFO (Last In First Out)
	stack = collections.deque()
	cd = threading.Condition()
	c1 = Consume(1)
	c2 = Consume(2)
	c3 = Consume(3)
	p = Produce()
	c1.start()
	c2.start()
	c3.start()
	p.start()
