'''
Created on 21-Jun-2016

@author: tcs
'''
#from collections import namedtuple
from FWtree.MyDict import MyDict
ff=open("rules.csv")
treeDict=MyDict()
for i in ff.readlines()[1:]:
    spl=i.split(",")
    src_ip,dest_ip,dest_port,action=spl[0],spl[1],str(spl[2]),spl[3][:-1]
    if treeDict.has_key(dest_ip):
        if treeDict[dest_ip].has_key(dest_port):
            if treeDict[dest_ip][dest_port].has_key(src_ip):
                pass
            else:
                treeDict[dest_ip][dest_port][src_ip]=action
        else:
            treeDict[dest_ip][dest_port]={src_ip:action}
    else:
        treeDict[dest_ip]={dest_port:{src_ip:action}}
print treeDict
    