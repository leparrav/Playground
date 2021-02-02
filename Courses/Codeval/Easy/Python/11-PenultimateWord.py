'''
https://www.codeeval.com/open_challenges/92/
'''
import sys

def main():
	with open(sys.argv[1],'r') as word_file:
		for line in word_file.readlines():
			print line.split()[-2]

if __name__ == '__main__':
    main()