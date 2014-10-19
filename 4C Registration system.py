par = map(int, raw_input().split(' '))

n = par[0]
names = {}

for i in range(n):
    name = raw_input()
    
    if name not in names:
        names[name] = 0
    else:
        names[name] += 1
    
    if names[name] == 0:
        print "OK"
    else:
        print name + str(names[name])
        