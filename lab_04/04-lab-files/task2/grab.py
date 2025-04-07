encrypted = [
    0x9b, 0x86, 0x91, 0x9e, 0x92, 0x96, 0x9c, 0xa0, 0x9e, 0x91,
    0x9e, 0x93, 0x86, 0x8c, 0x96, 0x8c, 0xa0, 0x96, 0x8c, 0xa0,
    0x8b, 0x97, 0x9a, 0xa0, 0x9d, 0x9a, 0x8c, 0x8b, 0xff
]

decoded = []
for b in encrypted:
    d = 255 - b
    decoded.append(d)

decoded_str = ''.join(chr(b) for b in decoded if b != 0)
print("flag:", decoded_str)


