'''
https://www.codeeval.com/open_challenges/39/
'''
import sys

def main():
	with open(sys.argv[1],'r') as word_file:
		for line in word_file.readlines():
			numbers = line.strip()
			attempts = 10
			result = 0
			for i in range(attempts):
				numbers = sum([pow(int(n),2) for n in str(numbers)])
				if numbers == 1:
					result = 1
					break
			print result

if __name__ == '__main__':
    main()