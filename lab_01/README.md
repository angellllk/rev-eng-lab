## Laboratory 01

**Prerequisites:**

```bash
sudo apt-get install strace ltrace
```

**Laboratory:**

- Started by using `ltrace` over the `obscure` binary.
  
  ```bash
  ltrace ./obscure
  ```

- From which we learn the expected input:
   ![Photo containing clues to the expected input](ss/obscure.png)

### Task 1: for Linux

**Prerequisites:**

- Install pwntools: 
  
  ```bash
  sudo apt-get update
  sudo apt-get install python3 python3-pip python3-dev git libssl-dev libffi-dev build-essential
  python3 -m pip install --upgrade pip
  python3 -m pip install --upgrade pwntools
  ```

**P1:** After running the code in `p1.py`, we can see the following output in the console:
![Photo containing output from p1.py](ss/p1.png)

**P2:** We wrap the process run inside the `ltrace` to get all the library functions that are called, thus the output after running the code in `p2.py`. We notice a call for `strlen` which gives us the clue that the program is checking for input's length. 
![Photo containing output from p2.py](ss/p2.png)

**P3:** By running the code in `p3.py`, we discover that the minimum length for the input string is `70`. 
![Photo containing output from p3.py](ss/p3.png)

By calling `p2.py`, but with a string of `70` characters, we obtain a **first substring** which we add to the payload that we'll use further.

![Photo containing p4.py output](ss/p4.png)

**P4:** We start constructing the payload by using the first substring found at `P3`. The code should look like this: 

```python
from pwn import * # sudo pip install pwntools


# start process interaction
# use "process" from pwntools
# wrap the process run inside "ltrace"
p = process("ltrace ./crackme", shell=True)

# send input
# use "send"/"sendline" from pwntools
# construct the payload based on findings.
payload = "zihldazjcn"

# add other payloads depending on the findings and adapt the "i"
# placeholder length on the way

# payload += "example_payload"
payload += 'i' * 50
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
```

After passing all the checks (obtaining all the substrings), we build our payload by combining all the found strings. We call the application once again by:

```bash
./crackme
```

and feed it our paylod which results the following output:

![Image containing the output of p4.py](ss/p4_final.png)

**P5:** Using the code in `p5.py`, we are able to obtain all the possible combinations of the previously obtained substrings. Being too large, we need to filter it by tossing away any verbosity and making the results less noisy. This is done with the solution written in `p5_result.py`. Reading over the `filtered_output.txt`, we find our flag at a specific candidate. 

![Photo containing the filtered output, identifying the flag](ss/filtered_output.png)

Using that candidate as payload to our `./crackme`, we can verify it works.

![Photo proof of valid candidate](ss/p5_final.png)


