from collections import Counter
cnt=Counter()
cnt["200.1.1.2"]+=100
cnt["200.1.1.3"]+=50
cnt["200.1.1.1"]+=40
cnt["200.1.1.0/24"]+=140
#print cnt
group1=[]
group2=[]
group3=[]
group4=[]
#from MyDict import MyDict,MyDic
from MyTree import treeDict,buildTree
buildTree()
for i in treeDict.keys():
    if (len(i.split("/"))==1):
        group1.append(i)
        continue
    if (i.split("/")[1]==str(24)):
        group2.append(i)
        continue
    if (i.split("/")[1]==str(16)):
        group3.append(i)  
        continue
    if (i.split("/")[1]==str(8)):
        group4.append(i)
        continue
g1len=len(group1)
g2len=len(group2)
g3len=len(group3)
g4len=len(group4)
counter=0
for i in group1:
    if treeDict.has_key(i):
        treeDict.insert(i,treeDict[i],index=counter)
        counter+=1
counter=g1len
for i in group2:
    if treeDict.has_key(i):
        treeDict.insert(i,treeDict[i],index=counter)
        counter+=1
counter=g2len
for i in group3:
    if treeDict.has_key(i):
        treeDict.insert(i,treeDict[i],index=counter)
        counter+=1
counter=g3len
for i in group4:
    if treeDict.has_key(i):
        treeDict.insert(i,treeDict[i],index=counter)
        counter+=1
print treeDict
group1=[]
group2=[]
group3=[]
group4=[]   
for i in list(cnt.most_common()):
    if (len(i[0].split("/"))==1):
        group1.append(i[0])
        continue
    if (i[0].split("/")[1]==str(24)):
        group2.append(i[0])
        continue
    if (i[0].split("/")[1]==str(16)):
        group3.append(i[0])  
        continue
    if (i[0].split("/")[1]==str(8)):
        group4.append(i[0])
        continue
print treeDict
counter=0
for i in group1:
    if treeDict.has_key(i):
        treeDict.insert(i,treeDict[i],index=counter)
        counter+=1
counter=g1len
for i in group2:
    if treeDict.has_key(i):
        treeDict.insert(i,treeDict[i],index=counter)
        counter+=1
counter=g2len
for i in group3:
    if treeDict.has_key(i):
        treeDict.insert(i,treeDict[i],index=counter)
        counter+=1
counter=g3len
for i in group4:
    if treeDict.has_key(i):
        treeDict.insert(i,treeDict[i],index=counter)
        counter+=1
print treeDict.keys()