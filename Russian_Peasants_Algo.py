import unittest
import random
import time
import timeit

def multiplier(num1, num2):
	sum = 0
	while(num1 > 0):
		if(num1 % 2 == 1): sum = sum + num2
		num1 = num1 >> 1
		num2 = num2 << 1
	return sum

class TestMultipler(unittest.TestCase):
	def test(self):
		a,b = random.randint(1, 65530), random.randint(1,65530)
		self.assertEqual(multiplier(23,4),92)
		self.assertEqual(multiplier(a,b),a*b)

# def MultiplierX(a, b):
#     x = a
#     y = b
#     sum = 0
#     while x > 0:
#         sum = sum + y
#         x = x-1
#     return sum


def performance():

	time_multiplier = timeit.timeit("multiplier(65530,65530)", setup="from __main__ import multiplier")
	time_calc = timeit.timeit("65530*65530")
	print(f"Russian Peasant Algorithm : Multiply (65530,65530)\nValue: {multiplier(65530,65530)}, Time: {time_multiplier}. \n")

	print(f"Simple Multiplication : Multiply (65530,65530)\nValue: {65530*65530}, Time: {time_calc}.")

	print(time_calc)




if __name__=="__main__":
	
	performance()
	unittest.main()
	# print(multiplier(12,2))
