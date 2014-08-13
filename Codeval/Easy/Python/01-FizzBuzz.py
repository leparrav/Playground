'''
Description: https://www.codeeval.com/open_challenges/1/
'''

import sys

def fb_converter(i,D1,D2):
	entry = ""
	if i % D1 == 0:
		entry += "F"
	if i % D2 == 0:
		entry += "B"
	return entry or i 

def main():
    with open(sys.argv[1]) as nf:
    	all_lines = nf.readlines()
    	for line in all_lines:
	    	line_list = line.split()
	    	D1 = int(line_list[0])
	    	D2 = int(line_list[1])
	    	N = int(line_list[2])
	    	line_print = [fb_converter(i,D1,D2) for i in range(1,N+1)]
	    	for x in line_print:
	    		print(x),
		print ("")



if __name__ == '__main__':
    main()