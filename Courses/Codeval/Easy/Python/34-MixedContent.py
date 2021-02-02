'''
https://www.codeeval.com/open_challenges/115/
'''
import sys
import re

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def main():
	with open(sys.argv[1],'r') as word_file:
		for line in word_file.readlines():
			line = line.strip()
			line_list = line.split(",")
			numbers = [c for c in line_list if is_number(c)]
			words = [c for c in line_list if not is_number(c)]
			if words and numbers:
				last = words[-1] + "|" + numbers[0]
				words.pop()
				words.append(last)
				merged = words + numbers[1:]
				print ",".join(merged)
			else:
				print line

			
if __name__ == '__main__':
    main()