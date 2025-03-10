#!/usr/bin/python

import itertools
from pwn import * # sudo pip install pwntools

# define all the substrings found
substrings = [
    "zihldazjcn",
    "vlrgmhasbw",
    "jqvanafylz",
    "hhqtjylumf",
    "yemlopqosj",
    "mdcdyamgec",
    "nhnewfhetk",
]

def try_candidate(candidate):
    """
    Starts the process and sends the candidate as payload.
    It prints the line read from the process and breaks when
    there are no lines left to read.
    """
    p = process("./crackme", shell=True)
    p.sendline(candidate)
    while True:
        try:
            line = p.readline()
            print("Read line: [%s]" % line)
        except:
            break
    p.close()
    print("")

# iterate through every possible permutation.
for perm in itertools.permutations(substrings):
    # construct the payload.
    candidate = "".join(perm)
    print("Trying candidate: %s" % candidate)
    # call the try_candidate function to start
    # the process and serve the payload.
    try_candidate(candidate)

