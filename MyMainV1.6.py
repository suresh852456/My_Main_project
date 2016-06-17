'''

@author: suresh Nagulavancha
'''
import pandas
import copy
from MyNode import Node
from MyTree import Tree
from MyDict import MyDict
def main():
	f=pandas.read_csv("rules.csv",header=0)
	global root
	global root_in
	global root_out
	global root_any
	global tree
	global levels
	levels=1
	root_any=copy.deepcopy(f)
	root_any.drop('inout',axis=1,inplace=True)
	root_in=f.groupby('inout').get_group('in')
	root_out=f.groupby('inout').get_group('out')
	levels+=1
	def createNew(df,dfname,grp):
		global levels
		levels+=1
		for i in df.groupby(grp).groups.keys():
			if i=="any":
				continue
			globals().update({dfname+"_"+i:df.groupby(grp).get_group(i)})
		temp=copy.deepcopy(df)
		temp.drop(grp,axis=1,inplace=True)
		globals().update({dfname+"_any":copy.deepcopy(temp)})
	createNew(root_in,"root_in","protocol")
	createNew(root_out,"root_out","protocol")
	createNew(root_any,"root_any","protocol")
	for k in globals().keys():
		if k.startswith('root_in_') or k.startswith('root_out_') or k.startswith('root_any_'):
			createNew(globals()[k],k,'dstip')
	for k in globals().keys():
		if k.startswith('root_') and len(k.split("_"))==4:
			createNew(globals()[k],str(k),'srcport')
	for k in globals().keys():
		if k.startswith('root_'):
			globals()[k]=globals()[k].values
	root=Node("root",root=True)
	for k in globals().keys():
		try:
			if k.startswith('root_'):
				globals().update({"$".join(k.split("_")):Node(k.split("_")[-1],value=globals()[k])})
		except KeyError:
			print "error occured for ",k
	tempdict=MyDict()
	tempdict=globals()
	templist=['root']
	count=2
	while(True):
		if count==levels:
			break
		for k in tempdict.keys():
			if k.startswith('root$') and len(k.split("$"))==count:
				templist.append(k)
			else:
				continue
		count+=1					
	for k in templist[1:]:
		try:
			globals()[k].set_parent(globals()["$".join(k.split("$")[:-1])])
		except KeyError:
			print "error occured for ",k
	tree=Tree(root)
	tree.buildTree()
	tree.printTree()
if __name__ == '__main__':
    main()
