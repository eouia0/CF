par = raw_input()
count = {}
for item in par:
    if item in count:
        count[item] += 1
    else:
        count[item] = 0

if len(count) % 2 == 0:
    print "CHAT WITH HER!"
else:
    print "IGNORE HIM!"