'''
https://www.codeeval.com/open_challenges/93/
'''
import sys

def main():
	with open(sys.argv[1],'r') as word_file:
		for line in word_file.readlines():
			line = line.strip()
			print " ".join([word[0].upper()+word[1:] for word in line.split()])

if __name__ == '__main__':
    main()