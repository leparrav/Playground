'''
https://www.codeeval.com/open_challenges/103/
'''
import sys

def coasterize(c,i):
	if i == 0 or i % 2 == 0:
		return c.upper()
	else:
		return c.lower()


def main():
	with open(sys.argv[1],'r') as word_file:
		not_char = [" ",".",",","!","'",":",";","?"]
		for line in word_file.readlines():
			i = 0
			coaster_line = []
			for c in line:
				if not c in not_char: 
					coaster_line.append(coasterize(c,i))
					i += 1
				else:
					coaster_line.append(c)
			print "".join(coaster_line)

if __name__ == '__main__':
    main()