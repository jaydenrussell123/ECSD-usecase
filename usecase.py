#!/usr/bin/python
import sys
import os
import re

#numerical script
def greater(a, b):
    #convert key to integer and compare
    if int(a[0]) > int(b[0]):
        return 1
    return -1

#removes leading 0 from numbers for better comparison
def stripzeroes(num):
    if (len(num)>1):
        j=0
        for i in num:
            if i=='0':
                j+=1
        #keeping everything on and past key 1
        num=num[j:]
    return num

#checking amount of arguments
if (len(sys.argv)<2):
    print '\nError, invalid number of arguments! Run with an argument of directory.'
    sys.exit()

#Get directory arguments
dir = sys.argv[1]
files=os.listdir(dir)
print "\nThe directory is: ",dir
#check if there are files in the directory
if (len(files)==0):
    print '\nYou need to have files in the directory!'
    sys.exit()
print "\nThe following files are in the directory: "
for file in files:
    print(file)

#loop each file name
matches = list()
notmatches= list()
filter= re.compile('^([0-9]+)(\.|)[A-z]+\.sql$', re.M|re.I)
for file in files:
    #apply regex
    matchObj = re.match(filter, file)
    #if match found
    if matchObj:
        num=matchObj.group(1)
        #check if first character 0
        num=stripzeroes(num)
        #append list
        matches.append( (num, matchObj.group()) )
    #incorrect here
    else:
        notmatches.append(file)
#sort matches
matches=sorted(matches , cmp=greater)
#print the matches
print '\nThe following file names are correct:'
for match in matches:
    print(match[1])

#sort unmatches
notmatches=sorted(notmatches)
#print the notmatches
print '\nThe following file names are incorrect:'
for notmatch in notmatches:
    print(notmatch)
