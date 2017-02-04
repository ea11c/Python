'''Eric Adams ea11c'''
from __future__ import print_function
import time
import sys

def log(output = sys.stdout):
	def log_function(func):
		def work(*args, **kwargs):
			sys.stdout = sys.__stdout__
			if output != sys.stdout:
				try:
					sys.stdout = open(output, "a")
				except TypeError:
					sys.stdout = sys.__stdout__
			print("\n")	
			print("Calling function ", func.__name__)
			if (len(args) + len(kwargs)) == 0:
				print("No arguments")
			else:
				print("Arguments: ")
				for item in args:
					print("\t- ", item, " of type ", type(item).__name__)
				for item in kwargs:
					print("\t- ", item, " of type ". type(item).__name__)
			print("Output:")
			p = time.time()
			result = func(*args, **kwargs)
			q = time.time()
			x = q - p
			s = format(x, '.5f')
			print("Execution time: ", s)
			if result is None:
				print("No return value.")
			else:
				print("Return value: ", result, "of type ", type(result).__name__)
		return work
	return log_function

