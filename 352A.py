n = map(int, raw_input().split())
a = map(int, raw_input().split())
t = sum(a)
if t < 5*9:
    if 0 in a:
        print 0
    else:
        print -1
else:
    if 0 in a:
        print "5"*(t//5//9*9)+"0"*a.count(0)
    else:
        print -1