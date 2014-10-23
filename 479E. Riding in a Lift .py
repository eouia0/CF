def nextlevel(n,a,b):
    sol = []
    for x in a:
        if x in before:
            ys = before[x]
        else:
            ys = range(max(1, 1+x-abs(x-b)), min(n,x+abs(x-b)))
            if x in ys:
                ys.remove(x)
            before[x] = ys
        sol.append(ys)
    return sol
    
par = map(int, raw_input().split(" "))
n, a, b, k = par[0], [par[1]], par[2], par[3]
MOD = 10**9 + 7

#count = [[1]]
total = 0
for t in range(k):
    sol = nextlevel(n, a, b)
    #print sol
    #print a
    #print count, total
    #print "\n"
    if len(sol) == 0:
        total = 0
        break
    else:
        #temp = []
        a = []
        total = 0
        for item in sol:
            if item != None:
                #temp.append(len(item))
                total += len(item)
                a += item
        #count.append(temp)

print total % MOD 
      