def cc(text,shiftBy):
    return ''.join(chr((ord(c) - 97 + shiftBy)% 26 +97) if c.islower() else c for c in text )

text = "abc"
shiftBy = 3
print(cc(text,shiftBy))