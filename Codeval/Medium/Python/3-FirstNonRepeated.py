'''
https://www.codeeval.com/open_challenges/12/
'''
import sys
from collections import Counter

def main():
	with open(sys.argv[1],'r') as word_file:
		for line in word_file.readlines():
			line = line.strip()
			c1 = Counter(line)
			for c in line:
				if c1[c] == 1:
					print c
					break

if __name__ == '__main__':
    main()