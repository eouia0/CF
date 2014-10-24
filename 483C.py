par = map(int, raw_input().split(" "))
n,k = par[0], par[1]#, par[2], par[3]

p1, p2, z = 1, n, n
while k > 0:
    if k % 2 == 0:
        print p2,
        p2 -= 1
    else:
        print p1,
        p1 += 1
    k -= 1
    z -= 1
for i in xrange(z):
    print p1,
    p1 += 1
    