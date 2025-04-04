## Laboratory 03

**Tasks**

**T1.** After opening the `riddle.c` file in Ghidra, we found the `main()` function at `FUN_154b()`.
![T1.1](ss/t1_1.png)

Based on the functions found in `riddle.c`, we start renaming the functions as:
| Function | Pseudocode |
| ----------- | ----------- |
| `setup()` | `FUN_1250()` |
| `gen_rand_string()` | `FUN_12E9()` |
| `chance()` | `FUN_14A6()` |
| `validate()` | `FUN_1441()` |

`validate()` was found in `chance()` while accessing every function before renaming, to check if there are other function calls.
![T1.2](ss/t1_2.png)
![T1.3](ss/t1_3.png)
![T1.4](ss/t1_4.png)

Result after renaming the functions:

![T1.5](ss/t1_5.png)

We proceed with the next part of renaming the stack variables in `setup()` and `main()`. 
- For `setup()`:
- ![T1.6](ss/t1_6.png)
- For `main()`:
- ![T1.7](ss/t1_7.png)

And for `chance()` and `gen_rand_string()` we have to rename the stack variables, inluding arrays:
- For `gen_rand_string()`
- ![T1.8](ss/t1_8_1.png) ![T1.8](ss/t1_8_2.png)
- For `chance()`:
- ![T1.9](ss/t1_9.png)

**T2.** We notice the following strings after running the program:

![T2.1](ss/t2_1.png)

We import the file into `Ghidra` and we analyze it. After finishing the process, we search for the first string we encountered by `Search - Memory` and we find the reference.

![T2.2](ss/t2_2.png)
![T2.3](ss/t2_3.png)

After renaming our functions, we get:

![T2.4](ss/t2_4.png)

The function that checks the password is:

![T2.5](ss/t2_5.png)

We double-click on the first element `DAT_004ca174` and then search for the first element of the alphabet at `004ca100`. By using:
- `Data - Terminate Unicode`, and
- `Data - Settings - Mutability - Constant`, 

our function will look like this:

![T2.6](ss/t2_6.png)

From which we learn what password the program expects. Those hex characters translate to `69F2a+18d346b/SQ5c65e`:

![T2.7](ss/t2_7.png)



