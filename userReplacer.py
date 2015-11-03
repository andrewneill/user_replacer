# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 15:53:22 2015

@author: aneill
"""

import os, getpass

print " \n \n \n"
print "This script will recursively find and replace a username or text in a directory. "
print "It is written specifically to search out for .xml and .id files for replacing"
print "the user in RS6 systems files."
print " "

print "WARNING: THIS WILL RECURSIVELY REPLACE ALL INSTANCES OF THE OLD USER WITH YOUR USERNAME!"
print "I highly recommend that you archive a working copy of the controller before running this script."
print " "
print "Note: It will find the old user name from the system.xml file. \n \n"

# read list of all files
#path = "G:/general/FILETRAN/AndrewNeill/ControllerTest/pythonTest"
path = '.'

# querry current user
newuser = getpass.getuser()
#newuser = "%%USUERNAME%%"
#newuser = "wolftech"

# figure out the old username
# basically, find "C:\Users\******\AppData..." and get everything in the *'s
print "Searching for old user"
olduser = ''
f = open("system.xml", 'r')
filedata = f.read()
location = filedata.find("C:\\Users\\")
location = location+9

i = 0
while True:
    if filedata[location+i] == '\\':
        break
    else:
        olduser += filedata[location+i]
        i=i+1

print "Replacing all instances of user %s with new user, %s \n" %(olduser, newuser) 

count = 0
countTotal = 0 
for path, subdirs, files in os.walk(path):
    for name in files:
        if name.endswith(".xml") or name.endswith(".id"):
            fi = os.path.join(path,name)
            f = open(fi, 'r+')
            filedata = f.read()
            f.close() #ran into errors when I tried to read and write. Had to close and reopen the file
                
            #replace data
            count = filedata.count(olduser)
            countTotal += count
            print "processing %s, %i instances found" %(fi, count)
            newdata = filedata.replace(olduser, newuser)
        
            # Write out the new data
            f = open(fi, 'w')
            f.write(newdata)
            f.close()

print " %i total instances of %s found and replaced with %s \n" %(countTotal, olduser, newuser)        
input( '\n Replacement complete. Press any key to exit.')
