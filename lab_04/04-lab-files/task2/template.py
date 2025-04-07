from pwn import *

context.arch = "amd64"
a = ELF.from_bytes( read("dump.txt") )
a.save("memorydump.elf")
