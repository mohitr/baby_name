from bs4 import BeautifulSoup

import requests
import string

'''
http://www.bachpan.com/Indian-Boy-Names-a.aspx
'''

max_page = 30 # for S

for l in string.uppercase:
	for i in range(1, max_page +1):	
		url = "http://www.bachpan.com/Indian-Boy-Names-%s.aspx?page=%s" % (l, i)

		r  = requests.get(url)
		data = r.text
		soup = BeautifulSoup(data, "lxml")

		for cell in soup.findAll("td", {"class": "c1"}):
			print cell.contents[1].contents[0].contents

