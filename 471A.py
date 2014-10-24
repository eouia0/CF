#n = input()
d = map(int, raw_input().split(" "))
#[s,t] = map(int, raw_input().split(" "))
b = sorted(d.count(x) for x in set(d))
if b[-1] < 4:
    print "Alien"
elif b[0] == 1:
    print "Bear"
else:
    print "Elephant"