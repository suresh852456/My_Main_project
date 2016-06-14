'''
Created on 10-Jun-2016

@author: Seeker
'''
from MyDict import MyDict
from MyNode import Node
class Tree:
    branches=MyDict()
    treeDict=MyDict()
    def __init__(self,root):
        self.root=root
        self.branches[self.root]=root.getTag()+"_"+str(root.num_children())
        self.treeDict[root.getTag()]=self.root
        #self.add_branches(root)
    def treeTraversal(self,traverse="search",printing=False):
        #count=0
        if traverse=="search":
            pass
    def buildTree(self):
        for v in Node.NodeIndex.values():
            self.addMyBranches(v)
    def printTree(self):
        for k in Node.NodeIndex.keys():
            self.printSubTree(k)
    def printSubTree(self,node="root"):
        if node in Node.NodeIndex.keys():
            if Node.NodeIndex[node].has_children():
                print "-----"*len(Node.NodeIndex[node].getTag().split("_"))+Node.NodeIndex[node].getTag().split("_")[-1]
                for i in Node.NodeIndex[node].get_child():
                    print "-----"*len(i.getTag().split("_"))+i.getTag().split("_")[-1]
    def getRoot(self,tag=False):
        if tag:
            return self.root.getTag()
        else:
            return self.root
    #DO this
    def BuildTreeDict(self):
        for j in range(self.treeDict.getSize()):
            temp1=self.treeDict.getKeyByIndex(j)
            ucount=len(temp1.split("_"))
            count=j
            for i in range(self.treeDict.getSize()):
                if temp1=="".join(self.treeDict.getKeyByIndex(i).split("_"))[:ucount]:
                    count+=1
                    self.treeDict.insert(self.treeDict.getKeyByIndex(i),self.treeDict.getValueByIndex(i),index=count)
    def add_branches(self,parent):
        def addit(parent):
                for i in parent.get_child():
                    self.branches[i]=i.getTag()+"_"+str(i.num_children())
        if not isinstance(parent, Node):
            return
        if parent.has_children():
            addit(parent)
            for i in parent.get_child():
                if isinstance(i, Node):
                    if i.has_children():
                        addit(i)
                    else:
                        self.add_branches(i)
        else:
            self.branches[parent]=parent.getTag()+"_"+str(parent.num_children())
    def addMyBranches(self,parent):
        if not isinstance(parent,Node):
            return
        if parent.has_children():
            for i in parent.get_child():
                    self.branches[i]=i.getTag()+"_"+str(i.num_children())
                    self.treeDict[i.getTag()]=i
        else:
            self.branches[parent]=parent.getTag()+"_"+str(parent.num_children())
            self.treeDict[parent.getTag()]=parent

