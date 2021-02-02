'''
https://www.codeeval.com/open_challenges/67/
'''
import sys

def hextodec(hex_string):
	letters = 'abcdef'
	dec = 0
	for i in range(len(hex_string)):
		current = hex_string[i]
		if current in letters:
			current = letters.index(current)+10
		dec += int(current)*pow(16,len(hex_string)-1-i)
	return dec

# def hexdec(c):
# 	letters = 'abcdef'
# 	if c in letters:
# 		return letters.index(c)+10
# 	else:
# 		return int(c)

def main():
	with open(sys.argv[1],'r') as word_file:
		for line in word_file.readlines():
			line = line.strip()
			hex_string = [c for c in line]
			#dec_string = [hexdec(c) for c in line]
			#print sum([dec_string[i]*pow(16,len(dec_string)-1-i) for i in range(len(dec_string))])
			print hextodec(hex_string)
			
if __name__ == '__main__':
    main()