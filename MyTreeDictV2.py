'''
Created on 21-Jun-2016
@author: tcs
'''
#from collections import namedtuple
from MyDict import MyDict
ff=open("rules2.csv")
treeDict=MyDict()
for i in ff.readlines()[1:]:
    spl=i.split(",")
    src_ip,dest_ip,dest_port,action=spl[0],spl[1],str(spl[2]),spl[3]
    if '\r\n' in action:
	action=action[:-2]
    if '\n' in action:
	action=action[:-1]
    if treeDict.has_key(dest_ip):
        if treeDict[dest_ip].has_key(dest_port):
            if treeDict[dest_ip][dest_port].has_key(src_ip):
                pass
            else:
                treeDict[dest_ip][dest_port][src_ip]=action
        else:
            if (src_ip=="*" or src_ip=="*.*.*.*" or src_ip=="any"):
		treeDict[dest_ip][dest_port]=action 
            else:
		treeDict[dest_ip][dest_port]={src_ip:action}
    else:
        treeDict[dest_ip]={dest_port:{src_ip:action}}
#print "Dest_ip"
#print treeDict.keys()
def printTree():
	for i in treeDict.keys():
		print i	
		for j in treeDict[i].keys():
			print "\t"+j
			if isinstance(treeDict[i][j],dict):
				for key in treeDict[i][j].keys():
					print "\t\t"+key+" "+treeDict[i][j][key]
			else:
				print "\t\t"+treeDict[i][j]
def checkrule(dest_ip,src_ip,dst_port):
	global treeDict
	if dest_ip in treeDict.keys():
		if dst_port in treeDict[dest_ip].keys():
			if isinstance(treeDict[dest_ip][dst_port],dict):
				if src_ip in treeDict[dest_ip][dst_port].keys():
					return treeDict[dest_ip][dst_port][src_ip]
				elif "*" in treeDict[dest_ip][dst_port].keys():
					return treeDict[dest_ip][dst_port]["*"]
				else:
					return "Deny"
			else:
				return treeDict[dest_ip][dst_port]
		elif "*" in treeDict[dest_ip].keys():
			if isinstance(treeDict[dest_ip]["*"],dict):
				if src_ip in treeDict[dest_ip]["*"].keys():
					return treeDict[dest_ip]["*"][src_ip]
				elif "*" in treeDict[dest_ip]["*"].keys():
					return treeDict[dest_ip]["*"]["*"]
				else:
					return "Deny"
			else:
				return treeDict[dest_ip]["*"]
		else:
			return "Deny"	
	elif "*" in treeDict.keys():
		if dst_port in treeDict["*"].keys():
			if isinstance(treeDict["*"][dst_port],dict):
				if src_ip in treeDict["*"][dst_port].keys():
					return treeDict["*"][dst_port][src_ip]
				elif "*" in treeDict["*"][dst_port].keys():
					return treeDict["*"][dst_port]["*"]
				else:
					return "Deny"
			else:
				return treeDict["*"][dst_port]
		elif "*" in treeDict["*"].keys():
			if isinstance(treeDict["*"]["*"],dict):
				if src_ip in treeDict["*"]["*"].keys():
					return treeDict["*"]["*"][src_ip]
				else:
					return "Deny"
			else:
				return treeDict["*"]["*"]
		else:
			return "Deny"
	else:
		return "Deny"
print checkrule("200.1.1.3","200.1.2.*","143")
printTree()
