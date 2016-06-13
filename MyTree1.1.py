'''
Created on 10-Jun-2016

@author: Seeker
'''
from MyDict import MyDict
from MyNode import Node

class Tree:
    branches=MyDict()
    #stringpr=""
    def __init__(self,root):
        self.root=root
        self.branches[self.root]=root.getTag()+"_"+root.getTag()+"_"+str(root.num_children())
        #self.add_branches(root)
    def treeTraversal(self,traverse="search",printing=False):
        #count=0
        if traverse=="search":
            pass
    def printTree(self):
        #doing this
        print self.getRoot(True)
        for k,v in self.branches.iteritems():
            if k.is_root():
                print v
                for i in range(k.num_children()):
                    print "|"
                    print "--"+str(i)
    def getRoot(self,tag=False):
        if tag:
            return self.root.getTag()
        else:
            return self.root
    def add_branches(self,parent):
        def addit(parent):
                for i in parent.get_child():
                    self.branches[i]=parent.getTag()+"_"+i.getTag()+"_"+str(i.num_children())
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
            self.branches[parent]=parent.get_parent().getTag()+"_"+parent.getTag()+"_"+str(parent.num_children())
    def addMyBranches(self,parent):
        if not isinstance(parent,Node):
            return
        if parent.has_children():
            #self.stringpr+=parent.getTag()
            for i in parent.get_child():
                    self.branches[i]=parent.getTag()+"_"+i.getTag()+"_"+str(i.num_children())
        else:
            self.branches[parent]=parent.get_parent().getTag()+"_"+parent.getTag()+"_"+str(parent.num_children())

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

for i in Node.NodeIndex.values():
    tr.addMyBranches(i)
    print i.getTag()+" : "+str(i.getLevel())

print tr.branches.values()

#tr.printTree()