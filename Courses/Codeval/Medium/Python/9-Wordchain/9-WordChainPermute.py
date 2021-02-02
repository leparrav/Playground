'''
https://www.codeeval.com/open_challenges/135/
'''
import sys
import itertools

def main():
	with open(sys.argv[1],'r') as word_file:
		for line in word_file.readlines():
			perm_gen = itertools.permutations(line.rstrip().split(","))
			chains = []
			for item in perm_gen:
				chain_length = 0
				for i in range(len(item)-1):
					if item[i][-1] == item[i+1][0]:
						chain_length += 1
				chains.append(chain_length)
			print max(chains)+1 if max(chains) != 0 else None


if __name__ == '__main__':
    main()