'''
https://www.codeeval.com/open_challenges/20/
'''
import sys

def lowerize(c):
	if c.isupper():
		return c.lower()
	else:
		return c

def main():
	with open(sys.argv[1],'r') as word_file:
		for line in word_file.readlines():
			text = [lowerize(c) for c in line.strip()]
			print "".join(text)

if __name__ == '__main__':
    main()