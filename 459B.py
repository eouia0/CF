n = input()
b = map(int, raw_input().split(" "))

'''
diff = {}
for i in range(len(b)):
    for j in range(i+1, len(b)):
        temp = abs(b[i] - b[j])
        if temp in diff:
            diff[temp] += 1
        else:
            diff[temp] = 1
print max(diff.keys()), diff[max(diff.keys())]
'''

'''
dic = {}
for item in b:
    if item in dic:
        dic[item] += 1
    else:
        dic[item] = 1

#dic = dict((i, b.count(i)) for i in b)
r = max(dic.keys())
l = min(dic.keys())
if r == l:
    print 0, dic[r]*(dic[r]-1)//2
else:
    print r-l, dic[r]*dic[l]
'''
r, l = max(b), min(b)
if r == l:
    print 0, n*(n-1)//2
else:
    print r-l, b.count(r)*b.count(l)