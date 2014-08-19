'''
https://www.codeeval.com/open_challenges/103/
'''
import sys

def main():
	with open(sys.argv[1],'r') as word_file:
		for line in word_file.readlines():
			unique = {}
			for number in line.split():
				if number not in unique:
					unique[number] = True
				elif number in unique:
					unique[number] = False
			lowest = "100"
			for key in unique:
				if unique[key] and int(key) < int(lowest):
					lowest = key
			if lowest != "100":
				print line.split().index(lowest)+1
			else:
				print "0"

if __name__ == '__main__':
    main()