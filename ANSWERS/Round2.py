import json
import pandas as pd

#Load Json into Dictionary
with open('Round2.json','r') as f:
    w=json.load(f)

list1=[]

#Since We want Three Column,We need to Create Nested List where each inner list should contain Three datas
#To convert To "OUT OF 100",Each mark is multiple by 10
for i in w['students']:
    list1.append([i['name'],i['class'],i['markOutOf10']*10])

#Convert the List into DataFrame
pf=pd.DataFrame(list1,columns=['Name','Class','Marks'])

#Finaly Convert The DataFrame to Excel
pf.to_excel('Round2.xlsx',index=False)

