'''
https://www.codeeval.com/open_challenges/113/
'''
import sys

def main():
	with open(sys.argv[1],'r') as word_file:
		for line in word_file.readlines():
			line = line.strip().split("|")
			v1 = line[0].split()
			v2 = line[1].split()
			print " ".join([str(int(a)*int(b)) for a,b in zip(v1,v2)])



if __name__ == '__main__':
    main()