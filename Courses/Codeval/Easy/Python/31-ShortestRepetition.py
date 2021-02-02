'''
https://www.codeeval.com/open_challenges/107/
'''
import sys

def main():
	with open(sys.argv[1],'r') as word_file:
		for line in word_file.readlines():
			line = line.strip()
			if line[0] in line[1:]:
				print line[1:].index(line[0])+1
			else:
				print len(line)
			
if __name__ == '__main__':
    main()