def longest(i, a, b, d, sol):
    #print i,  a[i]
    
    if b[i] != -1:
        return b[i]
    elif i == len(a) - 1:
        b[i-1] = 0
        return b[i-1]
    else:
        m = -1
        mi = -1
        for j in range(i+1, len(a)):
            if abs(a[j] - a[i]) >= d:
                temp = longest(j, a, b, d, sol)
                if 1 + temp > m:
                    m = 1 + temp
                    mi = j
        if mi != -1:
            b[i] = m
            sol[i] = mi
        return b[i]
            

par = map(int, raw_input().split(" "))
k, d = par[0], par[1]
a = map(int, raw_input().split(" "))
#b = [-1] * k


'''
print longest(0, a, b, d, sol)+1

output = ""

i = 0
while sol[i] == None:
    i += 1
output = output + str(i+1)

while sol[i] != None:
    output = output + " " + str(sol[i]+1)
    i = sol[i]
print output
'''

#b = [0] * k
c = [None] * k
dif = {}
dif[0] = [k-1]
keys = [0]
for i in range(k-2, -1, -1): 
    #print i, dif, keys
    diff = len(keys)-1
    index = 0
    
    while abs(a[i] - a[dif[keys[diff]][index]]) < d:
        #print diff, keys[diff], index
        index += 1
        if index == len(dif[keys[diff]]):
            index = 0
            diff -= 1
        if diff == -1:
            break
    
    #print i, diff, index
    #print c
    if diff >= 0:
        if diff + 1 in dif:
            dif[diff+1].append(i)
        else:
            dif[diff+1] = [i]
            keys.append(diff+1)
        c[i] = dif[keys[diff]][index]
        
        #b[i] = b[dif[diff][index]] + 1
    else:
        dif[0].append(i)
        
print c
print keys   
print dif
#print b


mK = max(dif.keys())

i = dif[mK][-1]
output = str(i+1)
count = 1
while c[i] != None:
    output = output + " " + str(c[i] + 1)
    i = c[i]
    count += 1
print count
print output

