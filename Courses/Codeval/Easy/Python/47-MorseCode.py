'''
https://www.codeeval.com/open_challenges/116/
'''
import sys

morseDict = {
'.-': 		'A',
'-...': 	'B',
'-.-.': 	'C',
'-..' : 	'D',
'.' : 		'E',
'..-.': 	'F',
'--.' : 	'G',
'....' :	'H',
'..' : 		'I',
'.---' : 	'J',
'-.-' : 	'K',
'.-..' : 	'L',
'--':		'M',
'-.':		'N',
'---':		'O',
'.--.':		'P',
'--.-':		'Q',
'.-.':		'R',
'...':		'S',
'-':		'T',
'..-':		'U',
'...-':		'V',
'.--':		'W',
'-..-':		'X',
'-.--':		'Y',
'--..':		'Z',
'.----':	'1',
'..---':	'2',
'...--':	'3',
'....-':	'4',
'.....':	'5',
'-....':	'6',
'--...':	'7',
'---..':	'8',
'----.':	'9',
'-----':	'0'
}

def main():
	with open(sys.argv[1],'r') as word_file:
		for line in word_file.readlines():
			line = line.strip()
			# Loop through the line
			last_char = ""
			word = []
			while(True):
				if " " in line:
					end = line.index(" ")
					#print end, word
					if line[:end]:
						word.append(morseDict[line[:end]])
					else:
						word.append(" ")
					line = line[end+1:]
				else:
					word.append(morseDict[line])
					break
			print "".join(word)


if __name__ == '__main__':
    main()