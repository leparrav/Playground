'''
https://www.codeeval.com/open_challenges/34/
'''
import sys

def main():
	with open(sys.argv[1],'r') as word_file:
		for line in word_file.readlines():
			content = line.strip().split(";")
			numbers, N = [int(c) for c in content[0].split(",")], int(content[1])
			size = len(numbers)
			to_print = []
			# Test all posible combinations
			for i in range(size):
				for j in range(size):
					if j != i:
						if numbers[i] + numbers[j] == N:
							to_append = ",".join(map(str,sorted([numbers[i],numbers[j]])))
							if to_append not in to_print:
								to_print.append(to_append)
			
			print ";".join(to_print) if to_print else "NULL"



if __name__ == '__main__':
    main()