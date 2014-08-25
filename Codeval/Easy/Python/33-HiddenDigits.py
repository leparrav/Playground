'''
https://www.codeeval.com/open_challenges/122/
'''
import sys

def main():
	with open(sys.argv[1],'r') as word_file:
		for line in word_file.readlines():
			line = line.strip()
			result = ""
			letters = "abcdefghij"
			nums = "0123456789"
			for c in line:
				if c in letters:
					result += str(letters.index(c))
				elif c in nums:
					result += c
			if result != "":
				print result 
			else:
				print "NONE"

			
if __name__ == '__main__':
    main()