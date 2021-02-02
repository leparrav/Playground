'''
https://www.codeeval.com/open_challenges/111/
'''
import sys

def main():
	with open(sys.argv[1],'r') as word_file:
		for line in word_file.readlines():
			line_list = line.split()
			len_words = [len(word) for word in line_list]
			max_val = max(len_words)
			print line_list[len_words.index(max_val)]

if __name__ == '__main__':
    main()