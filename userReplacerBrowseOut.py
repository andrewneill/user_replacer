# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 15:53:22 2015

@author: aneill

"""

import os, getpass, win32gui

from win32com.shell import shell, shellcon
# py2exe has an issue importing shell from win32, here's the fix:
# http://www.py2exe.org/index.cgi/win32com.shell







print " \n \n \n"
print "This script will recursively find and replace a username or text in a directory. "
print "It is written specifically to search out for .xml and .id files for replacing"
print "the user in RS6 systems files."
print " "

print "WARNING: THIS WILL RECURSIVELY REPLACE ALL INSTANCES OF THE OLD USER WITH YOUR USERNAME!"
print "I highly recommend that you archive a working copy of the controller before running this script."
print "You can press ctrl+c at any time to halt the program."
print " "
raw_input( '\n Press any key to begin.')

# Querry user for the system folder
#path = "G:/general/FILETRAN/AndrewNeill/ControllerTest/pythonTest"
desktop_pidl = shell.SHGetFolderLocation (0, shellcon.CSIDL_DESKTOP, 0, 0)
pidl, display_name, image_list = shell.SHBrowseForFolder (win32gui.GetDesktopWindow (),
  desktop_pidl,  "Choose the system folder",  0,  None,  None)
path = shell.SHGetPathFromIDList (pidl)
print path
os.chdir(path)

# querry current user
newuser = getpass.getuser()

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
        i += 1

# Ask if user wants to use automatic settings or not
print "You can press enter to replace all instances of %s with %s or" %(olduser, newuser)
arg = raw_input('type the text to search for and then be prompted again for the text to replace it with: \n')

if arg != '': # if user enters any text then that will be the replacement
    olduser = arg;
    newuser = raw_input('Please enter the text to replace %s with: \n' %(olduser))


# read list of all files and recursively replace user name
print "Replacing all instances of user %s with new user, %s \n" %(olduser, newuser) 
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
raw_input( 'Replacement complete. Press any key to exit.')
