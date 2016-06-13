# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 23:18:54 2016

@author: seeker
"""
from MyDict import MyDict
class DuplicateRootNode(Exception):
    '''Duplicate root node found'''
    pass
class NoParentException(Exception):
    '''No parent Node defined'''
    pass
class Node:
    NodeIndex=MyDict()
    rootset=False
    def __init__(self,tag,value=None,parent=None,data=None,root=False,level=0):
        self.tag=tag
        self.value=value
        self.data=data
        self.parent=parent
        self.root=root
        self.child=[]
        self.level=level
        if self.parent==None and self.root==False:
            raise NoParentException
        if root:
            if Node.rootset:
                raise DuplicateRootNode
            self.level=0
            Node.rootset=True
        else:
            self.level=self.parent.getLevel()+1
        if self.parent is not None:
            parent.add_child(self)
        self.NodeIndex[tag]=self
    def add_child(self,children,*args):
        self.child.append(children)
        if len(args)>0:
            for i in args:
                self.child.append(i)
    def num_children(self):
        return len(self.child)
    def get_child(self):
        return self.child
    def has_children(self):
        return True if len(self.child)!=0 else False
    def remove_child(self,children):
        if children in self.child:
            self.child.remove(children)
    def move_child(self,children,index):
        if children in self.child:
            self.child.remove(children)
            self.child.insert(index,children)
    def set_parent(self,parentnode):
        self.parent=parentnode
    def get_parent(self):
        return self.parent
    def is_leaf(self):
        if len(self.child)==0:
            return True
        else:
            return False
    def is_root(self):
        if self.parent==None:
            return True
        else:
            return False
    def getData(self):
        return self.data
    def getTag(self):
        return self.tag
    def getValue(self):
        return self.value
    def getLevel(self):
        return self.level
    def getAll(self):
        return self.tag,self.value,self.parent,self.child,self.data