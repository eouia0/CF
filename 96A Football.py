k = raw_input()
count = 1
prev = k[0]
flag = False
for item in k[1:]:
    if item == prev:
        count += 1
    else:
        prev = item
        count = 1
    if count == 7:
        flag = True
        break

if flag == True:
    print "YES"
else:
    print "NO"
