'''
Created on 21-Jun-2016
@author: tcs
'''
from collections import Counter
from MyDict import MyDic,MyDict
from netaddr import IPNetwork,IPAddress
ff=open("rules.csv")
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

def printTree(tree=None):
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
                            yield ip
                            yield dst_port
                            yield srcip
                            yield treeDict[ip][dst_port][srcip]
                            return
                        else:
                            continue
                else:
                    yield ip
                    yield dst_port
                    yield "0.0.0.0/0"
                    yield treeDict[ip][dst_port]
                    return 
            elif "*" in treeDict[ip].keys():
                if isinstance(treeDict[ip]["*"],MyDict):
                    for srcip in treeDict[ip]["*"].keys():
                        if checkMatch(src_ip,srcip):
                            yield ip
                            yield "*"
                            yield srcip
                            yield treeDict[ip]["*"][srcip]
                            return
                        else:
                            continue 
                else:
                    yield ip
                    yield "*"
                    yield "0.0.0.0/0"
                    yield treeDict[ip]["*"]
                    return 
            else:
                yield ip
                yield "*"
                yield "0.0.0.0/0"
                yield "Deny"
                return
    if "0.0.0.0/0" in treeDict.keys():
        if dst_port in treeDict["0.0.0.0/0"].keys():
            if isinstance(treeDict["0.0.0.0/0"][dst_port],MyDict):
                for srcip in treeDict["0.0.0.0/0"][dst_port].keys():
                    if checkMatch(src_ip, srcip):
                        yield "0.0.0.0/0"
                        yield dst_port
                        yield srcip
                        yield treeDict["0.0.0.0/0"][dst_port][srcip]
                        return
                    else:
                        continue
            else:
                yield "0.0.0.0/0"
                yield dst_port
                yield "0.0.0.0/0"
                yield treeDict["0.0.0.0/0"][dst_port]
                return
        elif "*" in treeDict["0.0.0.0/0"].keys():
            if isinstance(treeDict["0.0.0.0/0"]["*"],MyDict):
                    for srcip in treeDict["0.0.0.0/0"]["*"].keys():
                        if checkMatch(src_ip,srcip):
                            yield "0.0.0.0/0"
                            yield "*"
                            yield srcip
                            yield treeDict["0.0.0.0/0"]["*"][srcip]
                            return
                        else:
                            continue
            else:
                yield "0.0.0.0/0"
                yield "*"
                yield "0.0.0.0/0"
                yield treeDict["0.0.0.0/0"]["*"]
                return 
        else:
            yield "0.0.0.0/0"
            yield "*"
            yield "0.0.0.0/0"
            yield "Deny"
            return
    else:
        yield "0.0.0.0/0"
        yield "*"
        yield "0.0.0.0/0"
        yield "Deny"
        return 

def check(dst_ip,src_ip,dst_port):
    global dstipcounter
    global dstportcounter
    global srcipcounter
    dstip,dstport,srcip,action=checkrule(dst_ip,src_ip,dst_port)
    if dstip!="0.0.0.0/0":
        dstipcounter[dstip]+=1
    if dstport!="*":
        dstportcounter[dstport]+=1
    if srcip!="0.0.0.0/0":
        srcipcounter[srcip]+=1
    print dstip
    print dstport
    print srcip
    if action=="Accept" or action=="accept":
        return True
    else:
        return False
def reorderTree():
    global dstipcounter
    global srcipcounter
    global dstportcounter
    global treeDict
    pass
if __name__=="__main__":
    buildTree()
    dstipcounter=Counter()
    dstportcounter=Counter()
    srcipcounter=Counter()
    ff.close()
    printTree()
    #nfqueue.main()   #this method should run the main nethod
    #main will call this main
