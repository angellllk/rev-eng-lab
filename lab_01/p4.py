#!/usr/bin/python

from pwn import * # sudo pip install pwntools


# start process interaction
# use "process" from pwntools
# wrap the process run inside "ltrace"
p = process("ltrace ./crackme", shell=True)

# send input
# use "send"/"sendline" from pwntools
# construct the payload based on findings
payload = "zihldazjcn"
payload += "vlrgmhasbw"
payload += "jqvanafylz"
payload += "hhqtjylumf"
payload += "yemlopqosj"
payload += "mdcdyamgec"
payload += "nhnewfhetk"
p.sendline(payload)

# keep reading output until program terminates
while True:
	try:
		#use "readline" from pwntools
		line = p.readline()
		print ("Read line: [%s]" % line)

		#TODO
	except:
		#could not read line => program exited
		break


