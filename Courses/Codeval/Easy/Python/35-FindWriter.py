'''
https://www.codeeval.com/open_challenges/97/
'''
import sys

def main():
	with open(sys.argv[1],'r') as word_file:
		for line in word_file.readlines():
			if line != "":
				line = line.strip()
				content = line.split("|")
				encoded = content[0]
				key = content[1]
				writer = ""
				for value in key.split():
					writer += encoded[int(value)-1]
				print writer

			
if __name__ == '__main__':
    main()