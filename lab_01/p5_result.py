#!/usr/bin/env python3
import re


# noise defines the text from the output that we do not care about.
noise = [
    "Congrats. If that is the correct input you will now get a flag",
    "If all you see is garbage, try a different one"
]

def is_valid_flag(s):
    """
    Checks if the passed flag "s" is valid. A flag is valid if
    it doesn't contain many backslashes (\). A big number of
    appearances of this symbol determines an invalid flag (garbage).
    """
    return s.count('\\') <= 2

# read the output file.
with open("output.txt", "r") as f:
    lines = [line for line in f.readlines() if line.strip() != ""]

# group every line in blocks.
# every block starts with the line "Trying candidate:" and continues until meeting "[*] Stopping process".
blocks = []
current_block = []
for line in lines:
    stripped = line.strip()
    # if it's the beginning of the block:
    if stripped.startswith("Trying candidate:"):
        # if it's the current block:
        if current_block:
            blocks.append(current_block)
        current_block = [stripped]
    # if we're in the middle of the block:
    else:
        current_block.append(stripped)
        # if it's the final of the block:
        if "[*] Stopped process" in stripped:
            blocks.append(current_block)
            current_block = []
if current_block:
    blocks.append(current_block)

results = []
for idx, block in enumerate(blocks, start=1):
    candidate_str = None
    flag_candidate = None

    # search the line that contains the candidate
    for line in block:
        if line.startswith("Trying candidate:"):
            candidate_str = line[len("Trying candidate:"):].strip()
            break

    # search the line that contains the flag, found after "Read line:".
    for line in block:
        if line.startswith("Read line:"):
            # extract the flag
            m = re.search(r"Read line:\s*\[(.*)\]", line)
            if m:
                content = m.group(1).strip()
                # eliminate the b'' prefix.
                if (content.startswith("b'") and content.endswith("'")) or (
                        content.startswith('b"') and content.endswith('"')):
                    content = content[2:-1]
                # if content is not noise, we consider it a possible flag.
                if all(noise_str not in content for noise_str in noise):
                    flag_candidate = content
                    break

    # if we found both the flag and the candidate, add to the results.
    if candidate_str and flag_candidate and is_valid_flag(flag_candidate):
        results.append(f"Bloc {idx}: Candidate: {candidate_str} | Flag: {flag_candidate}")

# write the filtered data to another file.
with open("filtered_output.txt", "w") as outf:
    for line in results:
        outf.write(line + "\n")

print("Filtered output written to filtered_output.txt")

