'''
https://www.codeeval.com/open_challenges/112/
'''
import sys

def main():
	with open(sys.argv[1],'r') as word_file:
		for line in word_file.readlines():
			line = line.strip()
			contents = line.split(":")
			list_numbers = contents[0].split()
			keys = [n.split("-") for n in contents[1].split(",")]
			keys = [int(n) for l in keys for n in l]
			for i in xrange(0,len(keys),2):
				list_numbers[keys[i]],list_numbers[keys[i+1]] = list_numbers[keys[i+1]], list_numbers[keys[i]]
			print " ".join(list_numbers)

if __name__ == '__main__':
    main()