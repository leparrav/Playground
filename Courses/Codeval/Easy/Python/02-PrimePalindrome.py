'''
https://www.codeeval.com/open_challenges/3/
'''
import sys
import math

def isPalindrome(n):
	return n == int(str(n)[::-1])

def isPrime(n):
	limit = int(math.sqrt(n))+1
	for i in range(2,limit):
		if n % i == 0:
			return False
	return True

def main():
	#end = int(sys.argv[1])
	end = 1000
	for i in range(end,0,-1):
		if isPalindrome(i) and isPrime(i):
			print i
			break

if __name__ == '__main__':
    main()

