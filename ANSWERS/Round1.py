import os
import json

#Load json into Dictionary
with open("Round1\\Round1.json",'r') as f:
    Data=json.load(f)

#Create Folder To Store The Files
os.mkdir("Round1practice")

#Split the KEY,VALUE pair using items() and using for Loop for performing File Creation
##Note:
#For Each Iteration Key is a name of the file and Value is the content which should write inside

for File_Name,Content in Data.items():
    with open("Round1practice\\"+File_Name,'w') as f2:
        f2.write(Content)