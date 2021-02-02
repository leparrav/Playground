'''
https://www.codeeval.com/open_challenges/132/
'''
import sys
from collections import Counter

def main():
	with open(sys.argv[1],'r') as word_file:
		for line in word_file.readlines():
			line = line.strip().split(",")
			c1 = Counter(line)
			to_print = None
			for key in c1:
				if c1[key] > len(line)/2:
					to_print = key
					break
			print to_print

if __name__ == '__main__':
    main()