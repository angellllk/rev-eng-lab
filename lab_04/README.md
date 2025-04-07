## Laboratory 03

**Tasks**

**T1.** > Windows Task -- TBA

**T2.** We run the program.
[1](1.png)

After opening the program with `Ghidra`, we search in `Memory` for `Wrong`, but we have no references:
[2](2.png)

Using `ltrace` shows a different string, `Do not debug me`. 
[3](3.png)

We search for it in `Ghidra`, and we find it in the following function. We keep in mind the address after the `ptrace` call, `0x4011a8`:
[4](4.png)

We start `gdb-peda` over the executable and we setup a `breakpoint` at `0x4011a8`.
[5](5.png)
[6](6.png)

We trigger the program run and we arrive at the `breakpoint` set up earlier. We change the `rax` register, which is used at figuring if the program is debugged or not, to `0`. After using `continue`, we notice that the anti-debugging procedure is bypassed.
[7](7.png)

Coming back to `Ghidra`, we find our `main()` function (renamed after):
[8](8.png) 

By accessing the decryption function and reading through the `for-loop` arguments, we can establish the boundary addresses: 
- `0x4011c7` as the starting address, and
- `0x4012cb` as the ending address.
[9](9.png)

The address we're going to place our second `breakpoint` in `gdb` is:
[10](10.png)
[11](11.png)

We resume the program until our newly created `breakpoint` and we **dump** the memory into a `dump.txt`. 
[12](12.png)

By running `grab.py` (which converts the dumped bytes into readable data), we obtain the following result:
[13](13.png)
[14](14.png)
[15](15.png)

