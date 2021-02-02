import sys
import json
import re 
import math

def newTerm(tweet_list,scores):
	tweet_score = []
	for entry in tweet_list:
		if ("text" in entry): #and (entry["lang"] == "en"): 
			text = entry['text'].encode('UTF-8')  
			#print "Tweet: " + text
			text = text.split() # text is now a list with each word
			current_score = 0
			unknow_words = []
			for word in text:
				word = word.lower()
				word =  re.sub(r'[^\w\s]','',word) # remove punctuation
				if word in scores:
					current_score += scores[word]
					#print "Known scores: " + word + " " + str(current_score)
				else: #  UNKNOWN WORD HERE
					unknow_words.append(word)
					#print "Unknown score: " + word + " " + str(current_score)
			#print unknow_words
			for each in unknow_words:
				scores[each] = math.floor(current_score/len(text)*5.0) # Mean of tweeter words score x 3
				print each + " " + str(scores[each]) 
			tweet_score.append(current_score)
			#print "Tweet score: " + str(current_score)
		else: # If language is not english, score is 0
			tweet_score.append(0)


def hw(sent_file,tweet_file):
	afinnfile = sent_file
	scores = {} # initialize an empty dictionary
	for line in afinnfile:
		term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
		scores[term.lower()] = int(score)  # Convert the score to an integer.
	
	tweet_list = []
	for line in tweet_file:
		tweet_list.append(json.loads(line))

	newTerm(tweet_list, scores)

def main():
    dict_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw(dict_file,tweet_file)

if __name__ == '__main__':
    main()
