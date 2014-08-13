'''
https://www.codeeval.com/open_challenges/8/
'''
import sys

def reverse(s):
	list_words = s.split()
	print " ".join(list_words[::-1])

def main():
	with open(sys.argv[1]) as word_file:
		all_lines = word_file.readlines()
		for line in all_lines:  reverse(line)

if __name__ == '__main__':
    main()