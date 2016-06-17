'''
Created on 26-May-2016

@author: suresh Nagulavancha
'''
import pandas
import numpy
f=pandas.read_csv("rules.csv",header=0)
n=f.values #nd array
#print n
print n[1]
#g= f.groupby('in_out').groups.keys()
#k=f.groupby(['in_out','protocol','dst_port','dst_ip'])
#print k.get_group(('in','tcp','432','192.168.2.1'))
#for name,group in k:
#    print name
#    print group

#i=g.get_group('out')
#k=g.get_group('any')
#f

#print g.get_group('in')
#print g.get_group('tcp')
#print g.get_group('udp')
#print g.get_group('any')
if __name__ == '__main__':
    pass
