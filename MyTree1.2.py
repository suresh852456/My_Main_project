'''
Created on 10-Jun-2016

@author: Seeker
'''
from MyDict import MyDict
from MyNode import Node

class Tree:
    branches=MyDict()
    def __init__(self,root):
        self.root=root
        self.branches[self.root]=root.getTag()+"_"+str(root.num_children())
        #self.add_branches(root)
    def treeTraversal(self,traverse="search",printing=False):
        #count=0
        if traverse=="search":
            pass
    def printTree(self):
        #doing this
        #print self.getRoot(True)
        for k,v in self.branches.iteritems():
            if k.is_root():
                print v
                for i in range(k.num_children()):
                    print "|"
                    print "--"+str(i)
    def printSubTree(self,node="root"):
        if node in Node.NodeIndex.keys():
            print "I am new branch"
            print node
            print "My children are" 
            for i in Node.NodeIndex[node].get_child():
                print i.getTag()
            if len(Node.NodeIndex[node].get_child())==0:
                    print "No children"
    def getRoot(self,tag=False):
        if tag:
            return self.root.getTag()
        else:
            return self.root
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
        else:
            self.branches[parent]=parent.getTag()+"_"+str(parent.num_children())

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
for i,j in Node.NodeIndex.iteritems():
    tr.addMyBranches(j)
    tr.printSubTree(i)
print tr.branches.values()
#tr.printSubTree()