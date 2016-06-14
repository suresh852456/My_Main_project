#!/usr/bin/python
'''
author: Suresh Nagulavancha
'''
from MyNode import Node
from MyDict import MyDict
from MyTree import Tree
n1=Node("root",root=True)
n2=Node("in",parent=n1)
n3=Node("out",parent=n1)
n4=Node("any",parent=n1)
n5=Node("tcp",parent=n2)
n6=Node("tcp",parent=n3)
n7=Node("tcp",parent=n4)
n8=Node("udp",parent=n2)
n9=Node("udp",parent=n3)
n10=Node("udp",parent=n4)
n11=Node("hello",parent=n10)
n12=Node("world",parent=n11)
tr=Tree(n1)
#tr.printSubTree(i)
tr.buildTree()
#tr.printTree()
#print tr.branches.values()
#print tr.branches.getValueByIndex(0)
tempDict=MyDict()
for k,v in tr.treeDict.iteritems():
    tempDict[k]=v
#print tempDict.keys()
for i in range(tempDict.getSize()):
    temp1=tempDict.getKeyByIndex(i)
    ucount=len(temp1.split("_"))-1
    if not ucount:
        print temp1+":"+str(ucount)
        continue
    temp2="_".join(temp1.split("_")[:-1])
    
    print temp1+":"+str(ucount)
    print temp2