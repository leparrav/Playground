'''
https://www.codeeval.com/open_challenges/16/
'''
import sys

def tobin(x):
    return tobin(x/2) + [x%2] if x > 1 else [x]

def main():
	with open(sys.argv[1],'r') as word_file:
		for line in word_file.readlines():
			print tobin(int(line.strip())).count(1)

if __name__ == '__main__':
    main()