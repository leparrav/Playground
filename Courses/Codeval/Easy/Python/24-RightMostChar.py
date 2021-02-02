'''
https://www.codeeval.com/open_challenges/31/
'''
import sys

def main():
	with open(sys.argv[1],'r') as word_file:
		for line in word_file.readlines():
			line = line.strip()
			line = line.split(',')
			if line[1] in line[0]:
				print (len(line[0])-1)-line[0][::-1].index(line[1])
			else:
				print -1

if __name__ == '__main__':
    main()