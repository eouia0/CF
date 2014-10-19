par = map(int, raw_input().split(" "))
count = {}
for item in par:
    if item in count:
        count[item] += 1
    else:
        count[item] = 1

print 4 - len(count)