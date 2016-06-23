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
from MyDict import MyDict,MyDic
from MyTree import treeDict,buildTree,printTree
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
#print treeDict.keys()
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
#print treeDict
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
#print treeDict.keys()
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
#print treeDict.keys()
cnt1=Counter()
cnt1["80"]+=56
cnt1["56"]+=23
cnt1["22"]+=12
cnt1["443"]+=43
print cnt1
for i in  treeDict.keys():
	counter=0
	for j in treeDict[i].keys():
		if j!="*":
			treeDict[i].insert(j,treeDict[i][j],index=counter)
			counter+=1
dstp=[]
for i in cnt1.most_common():
	dstp.append(i[0])
print dstp
for i in  treeDict.keys():
	counter=0
	for k in dstp:
		for j in treeDict[i].keys():
			if j==k:
				treeDict[i].insert(j,treeDict[i][j],index=counter)
				counter+=1

printTree(treeDict)