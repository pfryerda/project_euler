#!/usr/bin/python

# Problem 1 of Project Euler

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

sum = 0
for i in range(1, 1000):
	if (i % 3 == 0 or i % 5 == 0):
		print("%s " % i)
		sum += i
print(sum)

# Alternative method

# def multipleOfFive(num):
# 	if (num % 5 == 0):
# 		return True
# 	else:
# 		return False

# def multipleOfThree(num):
# 	if (num % 3 == 0):
# 		return True
# 	else:
# 		return False

# sum = 0
# for i in range(1, 1000):
# 	if (multipleOfFive(i) or multipleOfThree(i)):
# 		print("%s " % i)
# 		sum += i
# print(sum)