#!/usr/bin/python
'''
@author: Suresh Nagulavancha
'''
from MyDict import MyDict
from MyNode import Node
class Tree:
    branches=MyDict()
    treeDict=MyDict()
    isBuild=False
    def __init__(self,root):
        self.root=root
        self.branches[self.root]=root.getTag()
        self.treeDict[root.getTag()]=self.root
        #self.add_branches(root)
    #Need To Do method
    def treeTraversal(self,traverse="search",printing=False):
        #count=0
        if traverse=="search":
            pass
    def buildTree(self):
        for v in Node.NodeIndex.values():
            self.addMyBranches(v)
        self.BuildTreeDict()
    def printTree(self,onlyvalues=False):
        if not self.isBuild:
            self.BuildTreeDict()
        if not onlyvalues:
            for i in self.treeDict.keys():
                print "   "*(len(i.split("_"))-1)+i
        else:
            for i in self.treeDict.keys():
                print "   "*(len(i.split("_"))-1)+i.split("_")[-1]
        
    def getRoot(self,tag=False):
        if tag:
            return self.root.getTag()
        else:
            return self.root
    def printSubTree(self,subkey):
        if not self.isBuild:
            self.BuildTreeDict()
        index=self.treeDict.indexofkey(subkey)
        print subkey
        length=len(subkey.split("_"))
        for j in range(index+1,self.treeDict.getSize()):
            if self.treeDict.getKeyByIndex(j).startswith(subkey):
                print "   "*(len(self.treeDict.getKeyByIndex(j).split("_"))-length)+self.treeDict.getKeyByIndex(j)
    def BuildTreeDict(self):
        self.isBuild=True
        for i in range(self.treeDict.getSize()):
            temp1=self.treeDict.getKeyByIndex(i)
            indexcount=i+1
            for j in range(self.treeDict.getSize()):
                if j<=i:
                    continue
                if "_".join(self.treeDict.getKeyByIndex(j).split("_")[:-1])==temp1:
                    self.treeDict.insert(self.treeDict.getKeyByIndex(j), self.treeDict.getValueByIndex(j), indexcount)
                    indexcount+=1
    #Duplicate method and waste can delete
    def add_branches(self,parent):
        def addit(parent):
                for i in parent.get_child():
                    self.branches[i]=i.getTag()
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
            self.branches[parent]=parent.getTag()
    def addMyBranches(self,parent):
        if not isinstance(parent,Node):
            return
        if parent.has_children():
            for i in parent.get_child():
                    self.branches[i]=i.getTag()
                    self.treeDict[i.getTag()]=i
        else:
            self.branches[parent]=parent.getTag()
            self.treeDict[parent.getTag()]=parent