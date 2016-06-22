'''
Created on 21-Jun-2016
@author: tcs
'''
from MyDict import MyDict,MyDic
from netaddr import IPNetwork,IPAddress
ff=open("rules2.csv")
treeDict=MyDict()
def convertIP(ipadd):
    if ("/" in ipadd) or ("*" not in ipadd):
        return ipadd
    if ipadd=="*":
        return "0.0.0.0/0"
    count=0
    temp=""
    for i in ipadd.split("."):
        if '*'==i:
            count+=1
            temp+="0."
        else:
            temp+=i+"."
    return temp[:-1]+"/"+str(32-count*8)
def checkMatch(ipadr,ipnet):
    if IPAddress(convertIP(ipadr)) in IPNetwork(convertIP(ipnet)):
        return True
    else:
        return False
def buildTree():
    for i in ff.readlines()[1:]:
        spl=i.split(",")
        src_ip,dest_ip,dest_port,action=convertIP(spl[0]),convertIP(spl[1]),str(spl[2]),spl[3]
        if '\r\n' in action:
            action=action[:-2]
        if '\n' in action:
            action=action[:-1]
        if treeDict.has_key(dest_ip):
            if treeDict[dest_ip].has_key(dest_port):
                if treeDict[dest_ip][dest_port].has_key(src_ip):
                    print "Redundant Rule found"
                    print "source ip,dest ip,dest port,action"
                    print src_ip,",",dest_ip,",",dest_port,",",action
                else:
                    treeDict[dest_ip][dest_port][src_ip]=action
            else:
                if (src_ip=="*" or src_ip=="*.*.*.*" or src_ip=="any"):
                    treeDict[dest_ip][dest_port]=action 
                else:
                    treeDict[dest_ip][dest_port]=MyDic({src_ip:action})
        else:
            treeDict[dest_ip]=MyDic({dest_port:MyDic({src_ip:action})})

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
    for ip in treeDict.keys():
        if checkMatch(dest_ip,ip):
            if dst_port in treeDict[ip].keys():
                if isinstance(treeDict[ip][dst_port],MyDict):
                    for srcip in treeDict[ip][dst_port].keys():
                        if checkMatch(src_ip,srcip):
                            return treeDict[ip][dst_port][srcip]
                else:
                    return treeDict[ip][dst_port]
            elif "*" in treeDict[ip].keys():
                if isinstance(treeDict[ip]["*"],MyDict):
                    for srcip in treeDict[ip]["*"].keys():
                        if checkMatch(src_ip,srcip):
                            return treeDict[ip]["*"][srcip]
                else:
                    return treeDict[ip]["*"]
            else:
                return "Deny"
    return "Deny" 

def main():
    buildTree()
    print checkrule("200.1.1.3","200.1.2.49","110")
if __name__=="__main__":
    buildTree()
    main()
    #print treeDict
