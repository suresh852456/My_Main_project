# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 21:20:14 2016

@author: seeker
"""

import struct

from netfilterqueue import NetfilterQueue
from re import findall
from subprocess import check_output
ifcnf= check_output(["ifconfig"])
cnf= findall("inet addr:.*",ifcnf)
for i in range(len(cnf)):
    if cnf[i].split()[1][5:]=='127.0.0.1':
        pass
    else:
        inet=cnf[i].split()[1][5:]
iptables_entrymaker=check_output(["iptables","-F"])
iptables_entrymaker=check_output(["iptables","-I","INPUT","-j","NFQUEUE","--queue-num","1"])


def ip_to_string(ip):
        return ".".join(map(lambda n: str(ip>>n & 0xff), [24,16,8,0]))

def print_and_accept(pkt):
        pl = pkt.get_payload()
        #print pl
        src_ip = struct.unpack('>I', pl[12:16])[0]
        dst_ip = struct.unpack('>I', pl[16:20])[0]
        tcp_offset = (struct.unpack('>B', pl[0:1])[0] & 0xf) * 4
        tmp = struct.unpack('>B', pl[tcp_offset+12:tcp_offset+13])[0]
        data_offset = ((tmp & 0xf0) >> 4) * 4
        src_port = struct.unpack('>H', pl[tcp_offset+0:tcp_offset+2])[0]
        data = pl[tcp_offset + data_offset:]
        print 'from {}:{},to {}'.format(ip_to_string(src_ip), src_port,ip_to_string(dst_ip))
        pkt.accept()

nfqueue = NetfilterQueue()
nfqueue.bind(1, print_and_accept)
try:
        nfqueue.run()
except KeyboardInterrupt:
        iptables_entrymaker=check_output(["iptables","-F"])
        print