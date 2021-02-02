import sys
import json

# This recursive function get the score and then returns it
# @param tweet a tweet text
# @param scores dictionary with possible scores
# \todo Need to finish this class
# def getScore(tweet,scores):
# 	# Base case only 1 word
# 	if len(tweet.split()) == 1:
# 		if tweet in scores:getScore
# 			return scores[tweet]
# 		else:
# 			return 0

# 	# Recursive case
# 	if tweet in scores:
# 		return scores[tweet]
# 	else:
# 		new_tweet = 0


def scoreTweet(json_content, scores):
	tweet_score = []
	for entry in json_content:
		current_score = 0
		if "text" in entry: # 
			if entry["lang"] == u"en": 
				text = entry['text'].encode('UTF-8')  
				for word in text.split(" "): # For each word in the text, get its score
					if word.lower() in scores:
						current_score += scores[word.lower()]
				tweet_score.append(current_score)
			else: # If language is not english, score is 0
				tweet_score.append(current_score)
		else: # If there is no text, score is 0
			tweet_score.append(current_score)
		print current_score

def hw(sent_file,tweet_file):
	afinnfile = sent_file
	scores = {} # initialize an empty dictionary
	for line in afinnfile:
		term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
		scores[term] = int(score)  # Convert the score to an integer.
	
	json_dicts = []
	for line in tweet_file:
		json_dicts.append(json.loads(line))

	scoreTweet(json_dicts, scores)

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw(sent_file,tweet_file)

if __name__ == '__main__':
    main()
