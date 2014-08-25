'''
https://www.codeeval.com/open_challenges/140/
'''
import sys
from collections import Counter

def main():
	with open(sys.argv[1],'r') as word_file:
		for line in word_file.readlines():
			line = line.strip()
			content = line.split(";")
			words = content[0].split()
			keys = [int(c) for c in content[1].split()]
			result = [None]*len(words)

			# Reconstruct 
			for k,w in map(None,keys,words):
				if k:
					result[int(k)-1] = w

			# Fill what's left
			c1 = Counter(words)
			c2 = Counter(result)
			diff = c1 - c2
			missing_word = list(diff.elements())[0]
			index = result.index(None)
			result[index] = missing_word
			
			print " ".join(result)



			
if __name__ == '__main__':
    main()