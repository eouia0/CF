''' 
def can(n, minT, maxT, total):
    ans = [-1 for i in range(n)]
    schedule(n, minT, maxT, total, ans)

        
    #print "ans", ans
    for item in ans:
        if item == -1:
            return "NO"
    
    return ans
    
    
def schedule(n, minT, maxT, total, ans):
    #print n, total, ans
    
    if sum(maxT[:n]) < total or sum(minT[:n]) > total:
        #print sum(minT), total, sum(maxT)
        return False
        
    if n == 0 and total == 0:
        return True
    
    if n == 0 or total == 0:
        return False
    
    flag = False
    for i in range(minT[n-1], maxT[n-1]+1):
        if schedule(n-1, minT, maxT, total-i, ans) == True:
            #print n-1, ": ",  i
            ans[n-1] = i
            flag = True
            break
    return flag
'''

def schedule(n, minT, maxT, total):
    if sum(minT) <= total <= sum(maxT):
        print "YES"
        
        total = total - sum(minT)
        i = 0
        
        while total != 0:
            if total >= maxT[i] - minT[i]:
                total = total - (maxT[i] - minT[i])
                minT[i] = maxT[i]
                i += 1
            else:
                minT[i] += total
                total = 0
 
        
        sol = ""
        for i in range(n):
            sol = sol + str(minT[i])
            if i != n-1:
                sol = sol + " "
        print sol
        
    else:
        print "NO" 
    

par = map(int, raw_input().split(' '))

n = par[0]
total = par[1]
minT = []
maxT = []

for i in range(n):
    par = map(int, raw_input().split(' '))
    minT.append(par[0])
    maxT.append(par[1])

'''
temp = can(n, minT, maxT, total)
if temp == "NO":
    print temp
else:
    print "YES"
    sol = ""
    for item in temp[:-1]:
        sol = sol + str(item) + " "
    sol += str(temp[-1])
    print sol
'''
schedule(n, minT, maxT, total)

