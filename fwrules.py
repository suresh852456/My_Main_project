'''
Created on 26-May-2016

@author: suresh Nagulavancha
'''
import pandas
f=pandas.read_csv("rules.csv",header=0)
g=f.groupby('proto')
print "tcp"
print g.get_group('tcp')
print g.get_group('udp')
print g.get_group('any')
if __name__ == '__main__':
    pass
h=f.groupby('action')
print h.get_group('deny')
print h.get_group('accept')
