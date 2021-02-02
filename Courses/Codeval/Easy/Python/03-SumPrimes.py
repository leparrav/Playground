'''
https://www.codeeval.com/open_challenges/4/
'''
import sys
import math

def isPrime(n):
	limit = int(math.sqrt(n))+1
	for i in range(2,limit):
		if n % i == 0:
			return False
	return True

def main():
	#end = int(sys.argv[1])
	end = 1000
	acc = 0
	pcount, i = 0, 2
	while(pcount < end):
		if isPrime(i):
			acc += i
			pcount += 1
		i += 1
	print acc

if __name__ == '__main__':
    main()
