#!/usr/bin/python

from pwn import *

# calls contains the function calls found when we called
# the process with 'ltrace'. These are valid while the current
# state of the application does not validate our input length.
calls = ['memset', 'fgets', 'strlen', 'puts', 'exit']

# counter
i = 0

# maintain workflow until we notice a different
# length of function calls. This means we triggered
# a different state of the application.
while len(calls) == 5:
    i += 1

    # start the process wrapped with ltrace.
    p = process('ltrace ./crackme', shell=True)

    # send input based on the counter to find out the 'strlen'.
    p. sendline("1" * i)

    p.wait_for_close()

    # reset calls list to check for new state, if applicable.
    calls = []

    # keep reading output until program terminates.
    while True:
        try:
            line = p.readline()

            # read lines that do not start with + or -.
            if line[0] != 43 and line[0] != 45:
                line_str = line.decode('utf-8', errors='ignore')
                pos = line_str.find('(')
                if pos != -1:
                    calls.append(line_str[:pos])

        except:
            break

print("Length: " + str(i))
print(calls)

