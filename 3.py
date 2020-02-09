import os
import shutil

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)
        

# Example
createFolder('./out/')
# Creates a folder in the current directory called data

source = os.listdir("./")
destination = "./out/"
for files in source:
    if files.endswith(".jpg"):
        shutil.move(files,destination)
