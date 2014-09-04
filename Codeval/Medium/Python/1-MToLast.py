'''
https://www.codeeval.com/open_challenges/10/
'''
import sys

def main():
	with open(sys.argv[1],'r') as word_file:
		for line in word_file.readlines():
			line = line.strip().split()
			if int(line[-1]) <= len(line):
				print line[-int(line[-1])-1]

if __name__ == '__main__':
    main()