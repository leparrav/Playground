'''
https://www.codeeval.com/open_challenges/27/
'''
import sys

def tobin(x):
    return tobin(x/2) + [str(x%2)] if x > 1 else [str(x)]

def main():
	with open(sys.argv[1],'r') as word_file:
		for line in word_file.readlines():
			print "".join(tobin(int(line.strip())))



if __name__ == '__main__':
    main()