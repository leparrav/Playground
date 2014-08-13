'''
https://www.codeeval.com/open_challenges/30/
'''
import sys

def main():
	with open(sys.argv[1],'r') as word_file:
		for line in word_file.readlines():
			lists = line.rstrip().split(';')
			first, second = [l.split(',') for l in lists]
			intersection = list(set(first).intersection(set(second)))
			intersection.sort()
			if len(intersection) >= 1: 
				print ','.join(intersection)
			else:
				print ""

if __name__ == '__main__':
    main()