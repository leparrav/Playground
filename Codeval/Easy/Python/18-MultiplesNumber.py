'''
https://www.codeeval.com/open_challenges/18/
'''
import sys

def main():
	with open(sys.argv[1],'r') as word_file:
		for line in word_file.readlines():
			if line != "":
				numbers = [int(s) for s in line.split(",")]
				i = 1
				while True:
					if numbers[1]*i > numbers[0]:
						print numbers[1]*i
						break
					else:
						i += 1
			else:
				print ""


if __name__ == '__main__':
    main()