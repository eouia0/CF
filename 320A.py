n = raw_input()
d = set(["1","14", "144"])

flag = "YES"
i = 0
while i < len(n):
    if n[i:i+3] in d:
        i += 3
    elif n[i:i+2] in d:
        i += 2
    elif n[i] in d:
        i += 1
    else:
        flag = "NO"
        break
print flag