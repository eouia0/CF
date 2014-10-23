a = raw_input()
d = set()
for item in a:
    if not item in "{}, ":
        d.add(item)
print len(d)