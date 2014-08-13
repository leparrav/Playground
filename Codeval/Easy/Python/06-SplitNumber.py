'''
https://www.codeeval.com/open_challenges/91/
'''
import sys

def main():
	with open(sys.argv[1]) as word_file:
		all_lines = word_file.readlines()
		for line in all_lines:
			number, pattern = line.split(" ")
			# Find the - or +
			if "-" in pattern:
				sign = "-1"
				cut = pattern.index("-")
			else:
				sign = "+1"
				cut = pattern.index("+")
			print int(number[:cut]) + int(sign)*int(number[cut:])
			


if __name__ == '__main__':
    main()