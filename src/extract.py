#@author - Eric Kingori
#this program will extract links from output files
#input designed for demo and testing purposes intergration into full sytem will not require user input

import os
#opens all text files in output directory
def openFiles(outputDir):
	for filename in os.listdir(outputDir):
		print "extracting links from: " + outputDir + "/"+ filename
		f = open(outputDir + "/"+ filename)
		read = f.readlines()
				
		for line in read:
			if (line[:5] == "Link:"):
				link = line[6:]
				print '	Opening: ' + link
				os.system("python Scraper/tagScraper.py " + link)
									
				
		f.close()

outputDir = "../output"
openFiles(outputDir)

