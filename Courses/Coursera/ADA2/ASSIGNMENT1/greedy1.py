'''
Question 1
In this programming problem and the next you'll code up the greedy algorithms from lecture for minimizing the weighted sum of completion times.. Download the text file here. This file describes a set of jobs with positive and integral weights and lengths. It has the format

[number_of_jobs]
[job_1_weight] [job_1_length]
[job_2_weight] [job_2_length]
...
For example, the third line of the file is "74 59", indicating that the second job has weight 74 and length 59. You should NOT assume that edge weights or lengths are distinct.

Your task in this problem is to run the greedy algorithm that schedules jobs in decreasing order of the difference (weight - length). Recall from lecture that this algorithm is not always optimal. IMPORTANT: if two jobs have equal difference (weight - length), you should schedule the job with higher weight first. Beware: if you break ties in a different way, you are likely to get the wrong answer. You should report the sum of weighted completion times of the resulting schedule --- a positive integer --- in the box below.

ADVICE: If you get the wrong answer, try out some small test cases to debug your algorithm (and post your test cases to the discussion forum)!

For this problem, use the same data set as in the previous problem. Your task now is to run the greedy algorithm that schedules jobs (optimally) in decreasing order of the ratio (weight/length). In this algorithm, it does not matter how you break ties. You should report the sum of weighted completion times of the resulting schedule --- a positive integer --- in the box below. 

Answer 1: 69119377652.0
Answer 2: 67311454237.0
'''

'''
@brief: It organizes the list of jobs in  a list of tuples like [job_score,job_weight, job_length]
'''
def scoredList1(jobs):
	score_jobs = []
	for each in jobs:
		weight = int(each[0])
		length = int(each[1])
		score = weight-length # Weight - length
		score_jobs.append((score,weight,length))
	return score_jobs

def scoredList2(jobs):
	score_jobs = []
	for each in jobs:
		weight = int(each[0])
		length = int(each[1])
		score = weight*1.0/length*1.0 # Weight - length
		score_jobs.append((score,weight,length))
	return score_jobs


def completionTime(schedule):
	rtime = 0
	accum_length = 0
	for each_job in schedule:
		weight = each_job[1]
		current_length = each_job[2]
		accum_length += current_length
		rtime += float(weight*accum_length)
	return rtime


'''
Here start Main program
'''
with open("jobs.txt") as jobs_file:
	number_of_jobs = jobs_file.readline()
	jobs = []
	for i in range(0,int(number_of_jobs)):
		jobs.append(jobs_file.readline().split())
	jobs_scores = scoredList2(jobs) # Change depends to score
	schedule = sorted(jobs_scores, reverse = True)
	print completionTime(schedule)
	print jobs_scores





