from datetime import datetime, timedelta
import os
import sys


# Usage: python sortt.py "Path" "Integer" "M\C"
# Path: Folder path
# Integer: Number of the days since creation\last modification date
# M\C: C- for creation date
       M for modification date
def getListOfFiles(dir_Name):
     
    # create a list of files and sub directories 
    # names in the given directory 
 
    listOfFile = os.listdir(dir_Name)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dir_Name, entry)
        allFiles.append(fullPath)
                 
    return allFiles  


dir_Name = str(sys.argv[1])
days = int(sys.argv[2])
sort_type = str(sys.argv[3])
flashback = datetime.now() - timedelta(days)
listOfFiles = getListOfFiles(dir_Name)


if sort_type == 'M' :
    sorted_by_modification_date = sorted(listOfFiles, key=os.path.getmtime) # sort files by last modified date
    # Print files sorted by last modification date
    for elem in sorted_by_modification_date: # iterate over sorted files
        time = datetime.fromtimestamp(os.path.getmtime(elem)).strftime('%Y-%m-%d %H:%M:%S') # get time stemp from file
        time = datetime.strptime(time,'%Y-%m-%d %H:%M:%S') # Convert str to datetime
        if time > flashback:
            print(time, elem)

elif sort_type == 'C':
    # Print files sorted by creation date
    sorted_by_creation_date = sorted(listOfFiles, key=os.path.getctime) # sort files by creation date
    for elem in sorted_by_creation_date: # iterate over sorted files
        time = datetime.fromtimestamp(os.path.getctime(elem)).strftime('%Y-%m-%d %H:%M:%S') # get time stemp from file
        time = datetime.strptime(time,'%Y-%m-%d %H:%M:%S') # Convert str to datetime
        if time > flashback:
            print(time, elem)
