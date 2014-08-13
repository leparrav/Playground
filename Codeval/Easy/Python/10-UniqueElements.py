'''
https://www.codeeval.com/open_challenges/29/
'''
import sys

def main():
	with open(sys.argv[1],'r') as word_file:
		for line in word_file.readlines():
			numbers = [int(n) for n in line.split(",")]
			nstrings = [str(n) for n in set(numbers)]
			print ",".join(nstrings)

if __name__ == '__main__':
    main()