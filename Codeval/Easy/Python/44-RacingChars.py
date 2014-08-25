'''
https://www.codeeval.com/open_challenges/136/
'''
import sys

def main():
	with open(sys.argv[1],'r') as word_file:
		checkpoint, gate, left_turn, right_turn, straight = "C", "_", "/", "\\", "|"
		last_index = -1
		for line in word_file.readlines():
			line = line.strip()
			# Get Checkpoint or Gate
			if checkpoint in line:
				index = line.index(checkpoint)
			else:
				index = line.index(gate)
			
			#Where to turn 
			if index == last_index or last_index == -1:
				print line[:index] + straight + line[index+1:]
			elif index < last_index:
				print line[:index] + left_turn + line[index+1:] 
			elif index > last_index:
				print line[:index] + right_turn + line[index+1:]

			last_index = index

if __name__ == '__main__':
    main()