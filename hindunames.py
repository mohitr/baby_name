from bs4 import BeautifulSoup

import requests
import string
import bs4

'''
http://hindunames.net/hindu-boy-names-1
total 173 pages
'''

for s in range(1, 174):
		url = "http://hindunames.net/hindu-boy-names-%s" % s
	
		r  = requests.get(url)
		data = r.text
		soup = BeautifulSoup(data, "lxml")

		t = soup.find("div", {"class": "table-responsive"}).contents[3].contents
		for i in range(3, len(t), 2):
			if t[i].find("a") != None:	# some page have google anlt
				print t[i].find("a").contents[0]

