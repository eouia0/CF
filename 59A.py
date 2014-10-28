s = raw_input()
upper, lower = 0, 0
for item in s:
    if item.islower():
        lower += 1
    else:
        upper += 1

if lower >= upper:
    s = s.lower()
else:
    s = s.upper()
print s