'''
https://www.codeeval.com/open_challenges/96/
'''
import sys

def main():
	with open(sys.argv[1],'r') as word_file:
		for line in word_file.readlines():
			line = line.strip().split(" ")
			for word in line:
				print "".join([c*(not (c.islower() or c.isupper()))+
								c.upper()*c.islower() + c.lower()*c.isupper() for c in word]),
			print("")

if __name__ == '__main__':
    main()