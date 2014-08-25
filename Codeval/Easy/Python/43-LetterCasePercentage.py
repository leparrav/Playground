'''
https://www.codeeval.com/open_challenges/147/
'''
import sys

def main():
	with open(sys.argv[1],'r') as word_file:
		for line in word_file.readlines():
			line = line.strip()
			lower = [c for c in line if c.islower()]
			upper = [c for c in line if c.isupper()]
			lratio = len(lower)*1.0/(len(line))*100
			uratio = len(upper)*1.0/(len(line))*100
			print "lowercase: {0:.2f}".format(lratio) + " uppercase: {0:.2f}".format(uratio)

if __name__ == '__main__':
    main()