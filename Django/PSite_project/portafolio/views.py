from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from portafolio.models import Job, Course
from random import shuffle

def decode(name_url):
	return name_url.replace('_', ' ')

def encode(name):
	return name.replace(' ','_')

'''
@brief: This view return the index page, it has a image gallery of jobs which is random and max = 6 jobs to be shown
'''
def index(request):
	context = RequestContext(request)
	jobs_count, jobs_list  = Job.objects.count(), list(Job.objects.all())
	shuffle(jobs_list)
	max_jobs = 6
	if jobs_count < 6:
		max_jobs = jobs_count
	jobs = []
	jobs_urls = {}
	for i in xrange(0,max_jobs-1,2):
		jobs_urls[jobs_list[i].company_name] = encode(jobs_list[i].company_name)
		jobs_urls[jobs_list[i].role] = encode(jobs_list[i].role)
		jobs_urls[jobs_list[i+1].company_name] = encode(jobs_list[i+1].company_name)
		jobs_urls[jobs_list[i+1].role] = encode(jobs_list[i+1].role)
		jobs.append([jobs_list[i],jobs_list[i+1]])
	context_dict = {'jobs': jobs, 'jobs_urls': jobs_urls}
	return render_to_response('portafolio/index.html', context_dict, context)

def courses(request):
	context = RequestContext(request)
	courses_list = list(Course.objects.order_by('end_date'))[::-1] # most recent first
	context_dict = {'courses' : courses_list}
	return render_to_response('portafolio/courses.html', context_dict, context)

def jobs(request):
	context = RequestContext(request)
	jobs_list = list(Job.objects.order_by('end_date'))[::-1] # most recent first
	context_dict = {'jobs_list' : jobs_list}
	return render_to_response('portafolio/jobs.html', context_dict, context)

