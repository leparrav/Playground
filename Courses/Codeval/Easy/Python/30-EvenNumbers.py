'''
https://www.codeeval.com/open_challenges/100/
'''
import sys

def main():
	with open(sys.argv[1],'r') as word_file:
		for line in word_file.readlines():
			line = line.strip()
			print int(int(line) % 2 == 0)
			
if __name__ == '__main__':
    main()