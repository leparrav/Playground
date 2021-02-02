'''
https://www.codeeval.com/open_challenges/62/
'''
import sys

def main():
	with open(sys.argv[1],'r') as word_file:
		for line in word_file.readlines():
			line = line.strip()
			numbers = line.split(",")
			numbers = [int(n) for n in numbers]
			print numbers[0] - numbers[1]*(numbers[0]/numbers[1])
			
if __name__ == '__main__':
    main()