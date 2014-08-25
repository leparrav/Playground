'''
https://www.codeeval.com/open_challenges/149/
'''
import sys

tobin = {
	"00": "1",
	"0": "0"
}

def main():
	with open(sys.argv[1],'r') as word_file:
		for line in word_file.readlines():
			line = line.strip().split()
			flag,number = [],[]
			for i in xrange(0,len(line)):
				if i % 2 == 0:
					flag.append(line[i])
				else:
					number.append(line[i])
			bin = []
			for i in xrange(0,len(number)):
				bin.append(tobin[flag[i]]*len(number[i]))
			print int("".join(bin),2)


if __name__ == '__main__':
    main()