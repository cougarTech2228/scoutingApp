#destroys data files
import sys, os

files = [f for f in os.listdir(".\\")]
#print(files)
for file in files:
    if file[-3:] == "dat":
        os.remove(file)
