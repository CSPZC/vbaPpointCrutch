#!/usr/bin/python
import sys
import subprocess

cmd = "sudo /var/intercepter-ng/./intercepter_ios 2 1 w /var/intercepter-ng/ -gw "
a = 0
k = 0
t = " -t"
tx_mask = [] 
tx = []
ap_addr = raw_input('Enter access point ip: ')
targ_val = raw_input('Enter number of targets): ')

for a in range(a, len(ap_addr)):
	tx_mask.append(ap_addr[a])
	if (ap_addr[a] == "."):
		k+=1
	elif (k == 2):
		break

k = 0
a+=2
for a in range(a, len(ap_addr)):
	tx.append(ap_addr[a])
	k+=1

cmd+=ap_addr


#list to int
targ_val = map(str,targ_val)
targ_val = ''.join(targ_val)
targ_val = int(targ_val)
tx = map(str,tx)
tx = ''.join(tx)
tx = int(tx)

tx_mask = map(str, tx_mask)
tx_mask = ''.join(tx_mask)

#ip generation
k = 0
for tx in range(tx, tx+targ_val):
	cmd += t + `tx` +' '+ str(tx_mask) + '.' + (`tx + 1`)

print cmd


#write run.sh
fileobject = open("/var/intercepter-ng/run.sh", 'w')
fileobject.write(cmd)
fileobject.close()

subprocess.call("chmod +x /var/intercepter-ng/run.sh", shell=True)
subprocess.call("/var/intercepter-ng/./run.sh", shell=True)