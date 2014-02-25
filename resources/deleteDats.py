#destroys data files
#this could be done more easily from the file manager or this could be a function in the app
import sys, os

files = [f for f in os.listdir(".\\")]
#print(files)
for file in files:
    if file[-3:] == "dat":
        os.remove(file)
