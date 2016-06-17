#!/usr/bin/python
'''
author: Suresh Nagulavancha
'''
from MyNode import Node
from MyTree import Tree
import pandas
def main():
    print "Firewall Started"
    fwrul=pandas.read_csv("rules.csv")
    global n1
    n1=Node("root",root=True)
    #count=2
    #in_outD=fwrul.groupby("in_out")
    #iface=fwrul.groupby("in_out").groups.keys()
    n2=0
    n3=0
    n4=0
    n5=Node("tcp",parent=n2)
    n13=Node("port",parent=n5)
    n6=Node("tcp",parent=n3)
    n7=Node("tcp",parent=n4)
    n8=Node("udp",parent=n2)
    n9=Node("udp",parent=n3)
    n10=Node("udp",parent=n4)
    n11=Node("hello",parent=n10)
    n12=Node("world",parent=n11)
    global tr
    tr=Tree(n1)
    #tr.printSubTree(i)
    tr.buildTree()
def printTree():
    global tr
    tr.printTree()  
if __name__=="__main__":
    main()     
#tr.treeDict.insert(tr.treeDict.getKeyByIndex(4),tr.treeDict.getValueByIndex(4),2)
#print tr.treeDict.keys()
#tr.BuildTreeDict()
#print tr.treeDict.keys()
#print tempDict.keys()