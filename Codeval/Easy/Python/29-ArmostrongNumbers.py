'''
https://www.codeeval.com/open_challenges/82/
'''
import sys

def main():
	with open(sys.argv[1],'r') as word_file:
		for line in word_file.readlines():
			line = line.strip()
			print int(line) == sum([pow(int(c),len(line)) for c in line])
			
if __name__ == '__main__':
    main()