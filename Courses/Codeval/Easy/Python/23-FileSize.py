'''
https://www.codeeval.com/open_challenges/26/
'''
import sys
import os

def main():
	file_path = sys.argv[1]
	statinfo = os.stat(file_path)
	print statinfo.st_size
	

if __name__ == '__main__':
    main()