'''
https://www.codeeval.com/open_challenges/104/
'''
import sys

word_digit = {
	"zero": 0,
	"one": 1,
	"two": 2,
	"three": 3,
	"four": 4,
	"five": 5,
	"six": 6,
	"seven": 7,
	"eight": 8,
	"nine": 9 }

def main():
	with open(sys.argv[1],'r') as word_file:
		for line in word_file.readlines():
			print "".join([str(word_digit[word]) for word in line.rstrip().split(";")])

if __name__ == '__main__':
    main()