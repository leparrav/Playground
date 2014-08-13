'''
https://www.codeeval.com/open_challenges/21/
'''
import sys

def main():
	with open(sys.argv[1]) as word_file:
		for line in word_file.readlines():
			print sum([int(n) for n in line if n != "\n"])
			
if __name__ == '__main__':
    main()