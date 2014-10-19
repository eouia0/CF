n = int(raw_input())
cc = raw_input()

remove = 0
prev = cc[0]
for c in cc[1:]:
    if c == prev:
        remove += 1
    else:
        prev = c
print remove