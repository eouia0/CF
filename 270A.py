n = input()
for i in range(n):
    x = input()
    if 360 % (180 - x) == 0:
        print "YES"
    else:
        print "NO"