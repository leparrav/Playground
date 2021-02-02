'''
https://www.codeeval.com/open_challenges/91/
'''
import sys

def main():
	with open(sys.argv[1]) as word_file:
		all_lines = word_file.readlines()
		num_sorted = []
		for line in all_lines:
			num_sorted.append(sorted([float(n) for n in line.split()]))
		
		for entry in num_sorted:
			for n in entry:
				print("%.3f" %n),
			print(" ")


if __name__ == '__main__':
    main()