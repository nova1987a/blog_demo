from django.shortcuts import render
from django.views import generic
from .models import Blog


# Create your views here.
"""
class BlogList(generic.ListView):
    queryset = Blog.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
"""
def blog_list(request):
	blogs = Blog.objects.filter(status=1)
	lucky_num = gather_nums()
	return render(request, 'index.html', {'blog_list':blogs, 'r_num':lucky_num})
    
class BlogDetail(generic.DetailView):
    model = Blog
    template_name = 'blog_detail.html'
"""
def get_lottery(request):
	get_lottery = lottery_list()
	# Pass the imported dict to the template
	return  render(request, 'lottery.html', {'d': get_lottery})

def get_random(request):
	luckynum = gather_nums()
	# Pass the imported dict to the template
	return  render(request, 'lottery.html', {'r': luckynum})
"""
###---       Web scraping area      ---###
import requests
from bs4 import BeautifulSoup as bs
import re
#from django.http import HttpResponse
from fake_useragent import UserAgent


## New web scraping method , read a single file and generate random numbers
import json
from random import randrange

## Open the record file
def gather_nums():
	input_file = '/home/w9saka5ulbu0/public_html/djdemo/blog/frequent_nums.dat'
	with open(input_file, "r") as f:
		data = f.read()
		nums = json.loads(data)
	first_num = randrange(0, nums[0])
	select_lst = []
	select_lst.append(first_num)
	## Select if diff of 2 number is larger than 4
	for i in range(len(nums)):
		if nums[i]-select_lst[len(select_lst)-1] > 4:
			select_lst.append(nums[i])

	random_lst = []
	for j in range(len(select_lst)-1):
		random_num = randrange(select_lst[j], select_lst[j+1])
		random_lst.append(random_num)
	
	final_dict = {"Most frequent number(s)":[], "Lucky number(s)":[]}
	final_dict.update({"Most frequent number(s)":nums, "Lucky number(s)":random_lst})
	return final_dict
