a = raw_input()
b = raw_input()

flag = True
if len(a) != len(b):
    flag = False
else:
    i = 0
    while i < len(a) and flag:
        if a[i] != b[len(b)-1-i]:
            flag = False
        else:
            i += 1
if flag == True:
    print "YES"
else:
    print "NO"



