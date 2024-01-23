###---       Web scraping area      ---###
from bs4 import BeautifulSoup as bs
import requests
import re
from random import randrange
import time
from datetime import datetime
from fake_useragent import UserAgent

def lottery_list():
	## Define the URL
	url = "https://www.pilio.idv.tw/ltobig/listbbk.asp"
	## import fake user agent with random mode, idea from https://weikaiwei.com/python/python-crawler-fake-useragent/
	ua = UserAgent()
	user_agent = ua.random
	## invoke into the header
	header_user = {'user-agent': user_agent}
	req = requests.get(url, headers=header_user)
#	req = requests.get(url)
	if req == None:
		delay_choices = [5,3,10,6]
		delay = random.choice(delay_choices)
		time.sleep(delay)
		req = requests.get(url, headers=header_user)


	soup = bs(req.text, "lxml")
	#print(soup)
	result = soup.find_all('b', class_=False, id=False)[4:44]	# find all tag with "b" and reserve list[4:44]
	data_list = []
	for j in result:
		data = str(j).replace('\xa0','')		 	#remove \xa0 tags
		pattern = re.compile('<.*?>')				#remove html tags
		data_mod = re.sub(pattern, '', data)
		data_list.append(data_mod)
	lott_dict = {}
	for i in range(0,len(data_list),5):
		data2 = data_list[i:i+5][3:]		# every 5 elements as a group, then remove 1st 3 elements
		data2[0:2] = [','.join(data2[0:2])]
		data2_mod = list(data2[0].split(','))	# make data2[0] into a string list
		data2_mod = [int(x) for x in data2_mod]	# make all element became 'int' in the list
#		print(data2_mod)
		new_element = {int(i/5):data2_mod}	# create an element
		lott_dict.update(new_element)		# add the elemnt into the dict		
#	print(lott_dict)	
	## Create a new list to calculate numbers appearing count
	new_lst = [0]*50	# calculating number's apperance
	freq_lst = []		# store number satisfying the condition
	for lst in lott_dict.values():
		for j in range(50):
			for k in lst:
				if k == j+1:
					new_lst[j] = new_lst[j] + 1	# Count
#	print(new_lst)
	for l in range(len(new_lst)):
		### if the number repeating more than 3 times, less than 5 times
		if new_lst[l] >= 3 and new_lst[l] < 5:
			freq_lst.append(l+1)
	print(freq_lst)
				
	with open("frequent_nums.dat", "w") as fdict:
		fdict.write(str(freq_lst))
		fdict.close()


if __name__ == '__main__':
	lottery_list()
	print('Finish web scraping')

