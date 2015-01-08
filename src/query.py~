'''
Created on Oct 23, 2014

@author: Cory
@author: Matt
'''

import urllib2
import urllib
import pprint
import os
from apiclient.discovery import build
from googleapiclient.errors import HttpError

def getSnippets(response):
    #iterate through the keys in the query response (dictionary)
    for key in response.keys():
        #items key holds the link information
        if key == "items":
            #iterate over the items dictionary
            for itemValue in response[key]:
                #iterate over the keys in that dictionary
                for itemKey in itemValue.keys():
                    #check for output directory
                    if not os.path.exists(outputDir):
                        os.makedirs(outputDir)
                    
                    #print snippet    
                    if itemKey == "snippet":
                        with open(outputDir + "/" + filename, "a") as fout:
                            fout.write("Snippet: " +
                                       repr(itemValue[itemKey]) +
                                       "\n")
            
                    #print if it is a link
                    elif itemKey == "link":
                        with open(outputDir + "/" + filename, "a") as fout:
                            fout.write("Link: " +
                                       itemValue[itemKey] +
                                       "\n\n")

#Add API-Keys to this list
api_keys = ["AIzaSyAqa0-CM0ZZ8hxTjLGZ52SxTZ9UjaTp72A", "AIzaSyCHwlWEjEcdeH1KRnmIi9fq5Dnx2JBeVRw"]

search_Engine_ID = "016745198537660285174:espiwqmbexg"

domain = "Information Technology"
jobSynonym = ["jobs", "occupations", "professions", "professionals"]
form = ["such as", "including", "like"]

currentKey = 0;

filename = domain + " Links.txt"
outputDir = "../output"

service = build("customsearch", "v1", developerKey=api_keys[currentKey])


#query = "\"* Jobs such as Software Engineer\""
for js in jobSynonym:
    for fm in form:
        query = "\"* " + domain + " " + js + " " + fm + "\""
        print "Query is: " + query

        try:
            response = service.cse().list(q = query, cx = search_Engine_ID).execute()
        except HttpError, HttpErrorArg:
            argString = str(HttpErrorArg)
            location = argString.find("returned \"Daily Limit Exceeded\"")
            
            if location != -1:
                print "Daily Limit of queries exceeded, switching API key"
                currentKey += 1
            
                if currentKey >= len(api_keys):
                    print "No Usable API keys remaining"
                    print "Exiting..."
                    exit()
            else:
                print HttpErrorArg
                print "Exiting..."
                exit()
            
            service = build("customsearch", "v1", developerKey=api_keys[currentKey])
            response = service.cse().list(q = query, cx = search_Engine_ID).execute()
        
        getSnippets(response)

print "done"
