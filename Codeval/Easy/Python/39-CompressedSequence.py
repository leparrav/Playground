'''
https://www.codeeval.com/open_challenges/128/
'''
import sys
from collections import Counter

def main():
	with open(sys.argv[1],'r') as word_file:
		for line in word_file.readlines():
			line = line.strip()
			line = line.split()
			last, count = "", 1
			lcount = []
			for i in xrange(0,len(line)):
				current = line[i]
				if i != 0:
					if current == last:
						count += 1
					else:
						lcount.append(count)
						lcount.append(last)
						count = 1
				last = current
			lcount.append(count)
			lcount.append(last)
			print " ".join(str(n) for n in lcount)


if __name__ == '__main__':
    main()