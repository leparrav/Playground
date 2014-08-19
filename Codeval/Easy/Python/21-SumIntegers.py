'''
https://www.codeeval.com/open_challenges/24/
'''
import sys

def main():
	with open(sys.argv[1],'r') as word_file:
			print sum([int(s_num) for s_num in word_file.readlines()])

if __name__ == '__main__':
    main()