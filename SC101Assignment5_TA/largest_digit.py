"""
File: largest_digit.py
Name: Ryan Kuo
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n: int, the maximum digit of which will be find by this function
	:return: int, the maximum digit of n
	"""
	if n < 0:  # turn negative integer into positive one
		n *= -1
	if n < 10:
		return n
	else:
		return max(find_largest_digit(n//10), n % 10)


if __name__ == '__main__':
	main()
