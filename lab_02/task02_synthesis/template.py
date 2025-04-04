from pwn import *


#choose assembly architecture
context.arch = "amd64"

#write assembly code
text = '''
start:
    mov rax, 201
    xor rdi, rdi
    syscall
    
    mov rdi, rax
    mov rax, 60
    syscall
'''

#assemble to machine code
machine_code = asm(text)

#integrate machine code into a virtual ELF file
elf = ELF.from_bytes(machine_code)

#save ELF file to disk
elf.save("output.elf")
