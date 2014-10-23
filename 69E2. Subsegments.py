par = map(int, raw_input().split(" "))
n, k = par[0], par[1]
'''
a = []
count = {}
sets = set()

for i in range(n):
    temp = input()
    a.append(temp)
    if not temp in count:
        count[a[i]] = 0

for i in range(k-1):
    count[a[i]] += 1
    if count[a[i]] == 1:
        sets.add(a[i])
    if count[a[i]] == 2:
        sets.remove(a[i])

for i in range(k-1, n):    
    count[a[i]] += 1
    if count[a[i]] == 1:
        sets.add(a[i])
    elif count[a[i]] == 2:
        sets.remove(a[i])
    
    #print sets
    
    if len(sets) == 0:
        print "Nothing"
    else:
        print max(sets)
    
    
    count[a[i-k+1]] -= 1
    if count[a[i-k+1]] == 1:
        sets.add(a[i-k+1])
    elif count[a[i-k+1]] == 0:
        sets.remove(a[i-k+1])
'''
a = []
count = {}
window = {}

for i in range(n):
    temp = input()
    a.append(temp)
    if not temp in count:
        count[a[i]] = 0

for i in range(k-1):
    count[a[i]] += 1
    if count[a[i]] == 1:
        window[a[i]] = 1
    elif count[a[i]] == 2:
        del window[a[i]]
        
for i in range(k-1, n):
    count[a[i]] += 1
    if count[a[i]] == 1:
        window[a[i]] = 1
    elif count[a[i]] == 2:
        del window[a[i]]
    
    #print window
    if len(window) == 0:
        print "Nothing"
    else:
        print max(window.keys())
    
    count[a[i-k+1]] -= 1
    if count[a[i-k+1]] == 1:
        window[a[i-k+1]] = 1
    elif count[a[i-k+1]] == 0:
        del window[a[i-k+1]]    