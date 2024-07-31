import os

#Create Three Different Folder For Each File Type
os.mkdir("TXT")
os.mkdir("JSON")
os.mkdir("CSV")

#Get List Of All Files In The Given Folder
All_FILE=os.listdir()

#Iterate Through Each file 
for Current_File in All_FILE:
    #Get The Extention
    ext=(Current_File.split(".")[-1])

    #If Extention Matches ,Files Are Moved To Its Respective Folder Using Replace() Method
    if(ext=="txt"):
        os.replace(Current_File,"TXT//"+Current_File)
    elif(ext=="json"):
        os.replace(Current_File,"JSON//"+Current_File)
    elif(ext=="csv"):
        os.replace(Current_File,"CSV//"+Current_File)
