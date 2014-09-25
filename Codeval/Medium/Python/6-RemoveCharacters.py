'''
https://www.codeeval.com/open_challenges/13/
'''
import sys

def main():
	with open(sys.argv[1],'r') as word_file:
		for line in word_file.readlines():
			content = line.strip().split(",")
			words, chars = content[0], content[1].strip()
			print "".join([c for c in words.strip() if c not in chars])

if __name__ == '__main__':
    main()