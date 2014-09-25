'''
https://www.codeeval.com/open_challenges/2/
'''
import sys

def getKey(item):
	return item[1]

def main():
	with open(sys.argv[1],'r') as word_file:
		unsorted_lines = []
		all_lines = word_file.readlines()
		N = int(all_lines[0])
		for line in all_lines:
			line = line.strip()
			unsorted_lines.append([line,len(line)])
		sorted_lines = sorted(unsorted_lines,key=getKey,reverse = True)
		for i in xrange(0,N):
			print sorted_lines[i][0]


if __name__ == '__main__':
    main()