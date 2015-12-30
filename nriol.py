from bs4 import BeautifulSoup

import requests
import string
import bs4

'''
http://www.nriol.com/babynames/baa.asp
'''

for l in string.lowercase:
		url = "http://www.nriol.com/babynames/b%s%s.asp" % (l, l)

		r  = requests.get(url)
		data = r.text
		soup = BeautifulSoup(data, "lxml")

		t = soup.find("div", {"class": "bNameList"}).contents[1].contents
		for i in range(3, len(t), 2):
			if type(t[i].contents[0]) != bs4.element.NavigableString: # N page has some google anlt code in end
				print t[i].contents[0].contents[0]

