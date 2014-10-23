par = map(int, raw_input().split(" "))
n, k = par[0], par[1]
   

'''
pop = 0

for i in range(n):
    temp = input()
    a.append(temp)
    
    if a[i] in count:
        count[a[i]] += 1
    else:
        count[a[i]] = 0
    
    if i >= k-1:
        maxN = None
        for key in count.keys():
            if key > maxN and count[key] == 1:
                maxN = key
        if maxN == None:
            print "Nothing"
        else:
            print maxN
        
        count[a[pop]] -= 1
        pop += 1
'''        

          
''' 
a = []
count = {}
for i in range(n):
    temp = input()
    a.append(temp)
    if not temp in count:
        count[temp] = 0


for i in range(k-1):
    count[a[i]] += 1
 

pop = 0
for i in range(k-1, n):
    count[a[i]] += 1
    maxN = None
    for key in count.keys():
        if count[key] == 1 and key > maxN:
            maxN = key
    if maxN == None:
        print "Nothing"
    else:
        print maxN
    
    count[a[pop]] -= 1
    pop += 1
'''
a = []
count = {}
for i in range(n):
    temp = input()
    a.append(temp)
    if i < k-1:
        if temp in count:
            count[temp] += 1
        else:
            count[temp] = 1
    else:
        pop = 0
        maxN = None
        if temp in count:
            count[temp] += 1
        else:
            count[temp] = 1
        for key in count.keys():
            if count[key] == 1 and key > maxN:
                maxN = key
            if maxN == None:
                print "Nothing"
            else:
                print maxN
        count[a[pop]] -= 1
        pop += 1
      

'''
for i in range(n-k+1):
    temp = {}
    for j in range(i, i+k):
        if a[j] in temp:
            temp[a[j]] = False
        else:
            temp[a[j]] = True
    
    maxN = None
    #print temp
    for key in temp.keys():
        if temp[key] == True and key > maxN:
            maxN = key
    if maxN == None:
        print "Nothing"
    else:
        print maxN
'''