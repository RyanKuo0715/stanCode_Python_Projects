"""
File: coin_flip_runs.py
Name: Ryan Kuo
-----------------------
This program should simulate coin flip(s)
with the number of runs input by users.
A 'run' is defined as consecutive results
on either 'H' or 'T'. For example, 'HHHHHTHTT'
is regarded as a 2-run result.
Your program should stop immediately after your
coin flip results reach the number of runs!
"""

import random as r


def main():
	"""
	simulate a random outcome of coin flip with a certain run
	"""
	print('Let\'s flip a coin!')
	run = int(input('Number of runs: '))
	flip_coin(run)


def flip_coin(run):
	"""
	:param run: int, the number of runs of the flip
	:return: the result of the flip
	"""
	count_run = 0
	if_run = False
	result = r.choice('HT')
	while True:
		if count_run == run:
			print(result)
			break
		result += r.choice('HT')
		if result[-1] == result[-2] and not if_run:
			count_run += 1
			if_run = True
		elif result[-1] != result[-2]:
			if_run = False


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == "__main__":
	main()
