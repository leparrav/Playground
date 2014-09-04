'''
https://www.codeeval.com/open_challenges/99/
'''
import sys
import re
import math

def main():
	with open(sys.argv[1],'r') as word_file:
		for line in word_file.readlines():
			line = line.strip().split()
			fixed = [int(re.sub('[(),]', '', entry)) for entry in line] 
			X = fixed[2]-fixed[0]
			Y = fixed[3]-fixed[1]
			print int(math.sqrt(pow(X,2)+pow(Y,2)))


if __name__ == '__main__':
    main()