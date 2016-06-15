#!/usr/bin/python
'''
author: Suresh Nagulavancha
'''
from MyNode import Node
#from MyDict import MyDict
from MyTree import Tree
n1=Node("root",root=True)
n2=Node("in",parent=n1)
n3=Node("out",parent=n1)
n4=Node("any",parent=n1)
n5=Node("tcp",parent=n2)
n13=Node("port",parent=n5)
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
tr.printSubTree("root_any_suresh")       
#tr.treeDict.insert(tr.treeDict.getKeyByIndex(4),tr.treeDict.getValueByIndex(4),2)
#print tr.treeDict.keys()
#tr.BuildTreeDict()
#print tr.treeDict.keys()
#print tempDict.keys()