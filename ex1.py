#!/bin/env python3
import threading

class SubThread(threading.Thread):
	def __init__(self):
		super().__init__()
		pass
	def run(self):
		print("run")

if __name__ == "__main__":
	# when 'run' is called ?
	sub = SubThread()
	sub.start()
