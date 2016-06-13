'''
Created on 10-Jun-2016

@author: seeker
'''
from collections import OrderedDict
class IndexNotFoundError(Exception):
    '''Index not available'''
    pass
class MyDict(OrderedDict):
    def __init__(self):
        super(MyDict, self).__init__()
    def insert(self,key,value,index=None,akey=None,bkey=None):
        tmp1=OrderedDict()
        tmp2=OrderedDict()
        if ((index is not None) and (isinstance(index, int))):
            if index<len(self.keys()):
                for i in self.iterkeys():
                    if self.indexofkey(i)<index:
                        tmp1[i]=self[i]
                    elif self.indexofkey(i)>=index:
                        tmp2[i]=self[i]
                self.clear()
                for i in tmp1.items():
                    self[i[0]]=i[1]
                self[key]=value
                for i in tmp2.items():
                    self[i[0]]=i[1]
                return self
            if index==len(self.keys()):
                self[key]=value
        if akey is not None:
            if akey in self.iterkeys():               
                self.insert(key,value,index=self.indexofkey(akey)+1)
            else:
                raise KeyError
        if bkey is not None:
            if bkey in self.iterkeys():
                self.insert(key, value, index=self.indexofkey(bkey))
            else:
                raise KeyError
                       
    def indexofkey(self,key):
        count=0
        for i in self.iterkeys():
            if i==key:
                return count
            else:
                count+=1
        raise KeyError
    def getKeyByIndex(self,index):
        count=0
        for i in self.iterkeys():
            if count==index:
                return i
            else:
                count+=1
        raise IndexNotFoundError
    def getValueByIndex(self,index):
        count=0
        for i in self.itervalues():
            if count==index:
                return i
            else:
                count+=1
        raise IndexNotFoundError
    def getKeyByValue(self,value):
        for k,v in self.iteritems():
            if v==value:
                return k
