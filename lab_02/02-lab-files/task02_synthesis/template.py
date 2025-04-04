from pwn import *


#choose assembly architecture
context.arch = "amd64"

#write assembly code
text = '''
start:
    mov rax, SYS_write
    mov rdi, 1
    mov rsi, hello
    mov rdx, 11
    syscall
hello: .asciz "hello world"
'''

#assemble to machine code
machine_code = asm(text)

#integrate machine code into a virtual ELF file
elf = ELF.from_bytes(machine_code)

#save ELF file to disk
elf.save("output.elf")
