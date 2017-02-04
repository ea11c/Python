'''Eric Adams ea11c'''
from __future__ import print_function

class Fibonacci:
	def __init__ (self, entries):
		self.nums = []
		self.index = 0
		if entries == 1:
			self.nums.append(0)
		elif entries == 2:
			self.nums.append(0)
			self.nums.append(1)
		else:
			i = 2
			self.nums.append(0)
			self.nums.append(1)
			while len(self.nums) != entries:
				self.nums.append(self.nums[i-1] + self.nums[i-2])
				i = i + 1

	def __str__ (self):
		return 'The first ' + str(len(self.nums)) + ' Fibonacci numbers are ' + str(self.nums)

	def __iter__(self):
		return self

	def next(self):
		if self.index >= len(self.nums):
			raise StopIteration
		val = self.nums[self.index]
		self.index = self.index + 1
		return val

	def get_nums(self):
		print(self.nums)
		return self.nums

def fibonacci_gen(entries):
	num = 0
	next_num = 1
	counter = 0
	while counter < entries:
		yield num	
		num = num + next_num
		next_num = num - next_num					
		counter = counter + 1

if __name__ == '__main__':
	f = Fibonacci(15)
	f.get_nums()
	print(Fibonacci(18))
	print ('testing for loop')
	for item in Fibonacci(12):
		print (item, end = ' ')
	print ('\ntesting fibonacci generator')
	for item in fibonacci_gen(8):
		print (item, end = ' ')
