'''
https://www.codeeval.com/open_challenges/103/
'''
import sys

def fibonacci(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	elif n > 1:
		return fibonacci(n-1) + fibonacci(n-2)

def main():
	with open(sys.argv[1],'r') as word_file:
		for line in word_file.readlines():
			print fibonacci(int(line))

if __name__ == '__main__':
    main()