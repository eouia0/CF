n = raw_input()
'''
if n[0] != "-":
    print int(n)
else:
    if len(n) == 2:
        print 0
    else:
        a1 = int(n[:-1])
        a2 = int(n[:-2]+n[-1])
        if a1 > a2:
            print a1
        else:
            print a2
'''
print max(int(n), int(n[:-1]), int(n[:-2]+n[-1]))
