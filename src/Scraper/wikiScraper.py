#@author - Eric Kingori
#this scraper is extract all body text from wikipedia.
#input designed for demo purposes and testing intergration into full sytem will not require user input

import urllib2
import urllib
import mechanize
from bs4 import BeautifulSoup

#set up the browser 
def browser():

	br = mechanize.Browser();
	br.set_handle_robots(False) 
	# spoof some headers so the request appears to be coming from a browser, not a bot
	headers = [("user-agent","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5)")]
	br.addheaders = headers
	return br

#creating the url link 
def url(query):
	query[0].capitalize()
	query = query.replace(" ","_")
	url = "http://en.wikipedia.org/wiki/" + query + "\n"
	print url
	return url



def get(br, url):
	#sending the request and storing the info
	try:	
		rawData = br.open(url).read()
		soup = BeautifulSoup(rawData)
		return soup
	except urllib2.HTTPError, e:
		print "HTTP Error code: " + str(e.code)
		if (e.code == 404):
			print "Wiki page not found"
		return False

	
	

def parse(soup):
	f = open('../../output/scrapedData.txt', 'w')
	info =soup.findAll('p')
	for paragraph in info:	
		f.write((paragraph.text + "\n").encode('UTF-8'))
	f.close()
	print("Done")


br = browser()
url = url(raw_input("Enter a Proffession: \n"))
soup = get(br, url)
if (soup != False):
	parse(soup)

