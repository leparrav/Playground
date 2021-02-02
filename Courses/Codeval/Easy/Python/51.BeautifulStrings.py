'''
https://www.codeeval.com/open_challenges/83/
'''
import sys
import re
from collections import Counter


def getKey(item):
	return item[1]

def main():
	with open(sys.argv[1],'r') as word_file:
		abc = "abcdefghijklmnopqrstuvwxyz"
		for line in word_file.readlines():
			line = line.strip().lower()
			line = "".join([c for c in line if c in abc])
			#print line
			c1 = Counter(line)
			l1 = [[n,c1[n]] for n in c1]
			l1 = sorted(l1,key=getKey,reverse=True)
			acc,beauty = 0,26
			for n in l1:
				acc += n[1]*beauty
				beauty -= 1
			print acc


if __name__ == '__main__':
    main()