#!/usr/bin/python
import sys
import os
import re
# print("no of arguments:")
# print(len(sys.argv))

#Get directory arguments
dir = sys.argv[1]
print "\nThe directory is: ",dir

print "\nThe following files are in the directory: "
files=os.listdir(dir)
for file in files:
    print(file)

#loop each file name
matches = list()
notmatches= list()
for file in files:
    filter= re.compile('^[0-9]+(\.|)[A-z]+\.sql$', re.M|re.I)
    #apply regex
    matchObj = re.match(filter, file)
    #if match found
    if matchObj:
        matches.append(matchObj.group())
    #incorrect here
    else:
        notmatches.append(file)

#print the matches
print '\nThe following file names are correct:'
for match in matches:
    print(match)

#print the notmatches
print '\nThe following file names are incorrect:'
for notmatch in notmatches:
    print(notmatch)
