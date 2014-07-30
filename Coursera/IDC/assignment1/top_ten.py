import json
import sys
import re

'''
Sort all hashtags obtained
'''
def quick_sort(p):
    if len(p) <= 1:
        return p

    pivot = p.pop(1)
    low,high = [],[]
    for entry in p:
        if entry[1] > pivot[1]:
            high.append(entry)
        else: 
            low.append(entry)
    return quick_sort(high) + [pivot] + quick_sort(low)


def getHash(tweet_list):
    hash_dict = {}
    for tweet in tweet_list: # A list of dict
        bprocess = False
        if ("text" in tweet) and ("entities" in tweet): # Process it
            bprocess = True
        if bprocess: 
            hash_list = tweet['entities']['hashtags'] 
            if hash_list != []:
                for item in hash_list:
                    hashtag = item["text"] 
                if hashtag in hash_dict:
                    hash_dict[hashtag] += 1
                else:
                    hash_dict[hashtag] = 1
    # Build a list with the dict..

    hash_list = []
    for word in hash_dict:
        hash_list.append([word,hash_dict[word]])

    hash_list = quick_sort(hash_list)
    
    for i in range(0,10):
        print hash_list[i][0]+ " " +str(hash_list[i][1])




def hw(tweet_file):
	tweet_list = []
	for line in tweet_file:
		tweet_list.append(json.loads(line))
	getHash(tweet_list)

def main():
    sys.setrecursionlimit(1000000) 
    tweet_file = open(sys.argv[1])
    hw(tweet_file)

if __name__ == '__main__':
    main()