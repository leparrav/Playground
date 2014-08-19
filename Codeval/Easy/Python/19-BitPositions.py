'''
https://www.codeeval.com/open_challenges/19/
'''
import sys

def tobin(x):
    return tobin(x/2) + [x%2] if x > 1 else [x]

def main():
	with open(sys.argv[1],'r') as word_file:
		for line in word_file.readlines():
			numbers = [int(x) for x in line.strip().split(",")]
			numbers[0] = tobin(numbers[0])
			print str(numbers[0][-numbers[1]]==numbers[0][-numbers[2]]).lower()

if __name__ == '__main__':
    main()