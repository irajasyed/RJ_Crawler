# coding: utf-8

# In[30]:

import csv


# In[59]:

import requests


# In[5]:

from BeautifulSoup import BeautifulSoup


# In[92]:


url = 'http://coe1.annauniv.edu/app/app_action/annauniv_results.php'
headers = { 'Authorization' : 'Basic ZW1zYXU6IUJlc3RHdW5AIzIwMTMh' } #k
start = 110111101001   #Enter starting roll no here
end = 110111101110      #Enter ending roll no here

# In[31]:
def get_results(start,end):
	with open('res_sub.csv', 'wb') as csvfile:
		spamwriter = csv.writer(csvfile)
		for i in range(start,end):
			regno= {'regno':i}
			r = requests.post(url,headers=headers, data=regno)
			soup = BeautifulSoup(r.text)
			if not soup.nexttonextresponse is None:
				spamwriter.writerow([soup.nextresponse.findAll('val')[0]['value'],soup.nextresponse.findAll('val')[1]['value'],soup.nexttonextresponse.findAll('response')[0]['value2'],soup.nexttonextresponse.findAll('response')[1]['value2'],soup.nexttonextresponse.findAll('response')[2]['value2'],soup.nexttonextresponse.findAll('response')[3]['value2'],soup.nexttonextresponse.findAll('response')[4]['value2'],soup.nexttonextresponse.findAll('response')[5]['value2'],soup.nexttonextresponse.findAll('response')[6]['value2'],soup.nexttonextresponse.findAll('response')[7]['value2'],
									 soup.findAll('response')[-1].val['def'].rsplit(None, 1)[-1]])

get_results(start,end)
