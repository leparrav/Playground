import sys
import json
import re 
import math

def frequency(tweet_list):
	tweet_score = []
	frequency = {}
	word_count = 0
	for entry in tweet_list:
		if ("text" in entry) and (entry["lang"] == "en"): 
			text = entry['text'].encode('UTF-8')  
			text = text.split() # text is now a list with each word
			current_score = 0
			for word in text:
				word = word.lower()
				word =  re.sub(r'[^\w\s]','',word) # remove punctuation
				if word in frequency:
					frequency[word] += 1
				else: #  UNKNOWN WORD HERE
					frequency[word] = 1
			word_count += 1
	for item in frequency:
		frequency[item] = frequency[item]*1.0/word_count
		print item + " " + "%.10f" %frequency[item]


def hw(tweet_file):
	tweet_list = []
	for line in tweet_file:
		tweet_list.append(json.loads(line))
	frequency(tweet_list)

def main():
    tweet_file = open(sys.argv[1])
    hw(tweet_file)

if __name__ == '__main__':
    main()
