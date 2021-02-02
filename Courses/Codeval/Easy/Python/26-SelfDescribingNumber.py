'''
https://www.codeeval.com/open_challenges/40/
'''
import sys

def main():
	with open(sys.argv[1],'r') as word_file:
		for line in word_file.readlines():
			result = 1
			line = line.strip()
			line = [int(c) for c in line]
			for i in range(len(line)):
				if line[i] != line.count(i):
					result = 0
					break
			print result

if __name__ == '__main__':
    main()