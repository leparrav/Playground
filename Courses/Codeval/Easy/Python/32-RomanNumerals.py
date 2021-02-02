'''
https://www.codeeval.com/open_challenges/106/
'''
import sys

values_13 = {
	0 : "I", 
	1 : "X",
	2 : "C",
	3 : "M" 
}

values_4 = {
	0 : "VI", # 4
	1 : "LX", # 40
	2 : "DC", # 400
}

values_5 = {
	0 : "V", # 5
	1 : "L", # 50
	2 : "D"  # 500
}

values_58 = {
	0 : "I",
	1 : "X",
	2 : "C"
}

values_9 = {
	0 : "XI", # 9
	1 : "CX", # 90
	2 :	"MC"  # 900
}

def main():
	with open(sys.argv[1],'r') as word_file:
		for line in word_file.readlines():
			dec_num = int(line.strip()) 
			dec_print = dec_num
			rom_num = ""
			for i in range(len(str(dec_num))):
				digit = dec_num % 10
				dec_num = dec_num/10
				if digit <= 3:
					rom_num += values_13[i]*digit
				elif digit == 4:
					rom_num += values_4[i]
				elif digit >= 5 and digit <= 8:
					rom_num += (digit-5)*values_58[i] + values_5[i] 
				elif digit == 9:
					rom_num += values_9[i]
			#print str(dec_print) + ": " + rom_num[::-1]
			print rom_num[::-1]

			
if __name__ == '__main__':
    main()