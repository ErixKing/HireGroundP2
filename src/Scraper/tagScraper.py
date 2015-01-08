#@author - Eric Kingori
#this scraper is extract all text from most websites based on html tags
#input designed for demo and testing purposes intergration into full sytem will not require user input
#output will also be modified from print statements to data written to a file

import sys
import urllib
import urllib2
import mechanize
from bs4 import BeautifulSoup

#This Function sets up the browser 
def browser():
	br = mechanize.Browser();
	br.set_handle_robots(False)
	headers = [("user-agent","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5)")]
	br.addheaders = headers
	return br


#This function sends the request and stores the info from the into an object
def openLink(br,url):	
	try:	
		rawData =  br.open(url).read()
		soup = BeautifulSoup(rawData)
		return soup
	except urllib2.HTTPError, e:
		print "HTTP Error code: " + str(e.code)
		if (e.code == 404):
			print "Page not found"
		return False

#This function extracts data from an object and save it to the output file
def extractText(soup):
	f = open('../../output/scrapedData.txt', 'w')
	tagList = ['li', 'strong', 'p', 'body', 'em', 'i', 'label', 'title', 'u' ]
	for tag in tagList:	
		info =soup.findAll(tag)
		for paragraph in info:
			f.write((paragraph.text).encode('utf-8'))
	
	f.close()
	print("Done")


#calling the defined functions
br = browser()

if (len(sys.argv)==1):
	print 'Usage: ' + sys.argv[0] +' [URL]'
	sys.exit(2)
else:
	url = sys.argv[1]
	print url[-4:] 
	if (url[-4:] == ".pdf"):
		print 'Cannot extract text from pdfs'
		sys.exit(2)
	
print url
#url = str(raw_input("enter or paste url to be opened: \n"))
soup = openLink(br, url)
if (soup != False):
	extractText(soup)

