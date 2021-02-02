'''
https://www.codeeval.com/open_challenges/102/
'''
import sys
import json

def main():
	with open(sys.argv[1],'r') as word_file:
		json_list = []
		for line in word_file.readlines():
			json_list.append(json.loads(line))

		for item in json_list:
			acc = 0
			for entry in item["menu"]["items"]:
				if entry:
					if "label" in entry:
						acc += entry["id"]
			print acc

if __name__ == '__main__':
    main()