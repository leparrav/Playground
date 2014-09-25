'''
https://www.codeeval.com/open_challenges/46/
Not happy about this solution, memory overflow for very large primes nubers
'''
import sys
import math

def primality(n, primes):
	if n <= 1 or n % 2 == 0:
		return False
	if n == 2:
		return True

	for i in range(3,int(math.sqrt(n))+1,2):
		if i in primes:
			if primes[i]:
				if n % i == 0 and n != i:
					return False
		elif i > max(primes):
			if n % i == 0 and n != i:
				return False
	return True

def main():
	with open(sys.argv[1],'r') as word_file:
		primes = {}
		for line in word_file.readlines():
			limit = int(line.strip())
			assert limit < 4294967295
			if limit > 2:
				to_print = [2]

				# print primes numbers up to N
				for i in range(1,limit,2):
					if i in primes:
						if primes[i]:
							to_print.append(i)
					else:
						primes[i] = primality(i, primes)
					 	if primes[i]:
					 		to_print.append(i)

		 		print ",".join(map(str,to_print))
		 	else:
		 		print ""

if __name__ == '__main__':
    main()