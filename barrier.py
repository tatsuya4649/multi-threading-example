#!/bin/env python
"""
	Barrier Control
"""
import threading
import time



class Gate(threading.Thread):
	def run(self):
		global barrier
		try:
			print(f"wait => {barrier.n_waiting}")
			barrier.wait()
			print("Go!!!")
		except threading.BrokenBarrierError:
			print("broken error")

if __name__ == "__main__":
	barrier = threading.Barrier(4)
	g1 = Gate()
	g2 = Gate()
	g3 = Gate()
	g4 = Gate()

	g1.start()
	time.sleep(1)
	g2.start()
	time.sleep(1)
	g3.start()
	time.sleep(1)
	g4.start()
