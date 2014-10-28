[r,c] = map(int, raw_input().split())
'''
cake = []
srow = []
scol = []
for i in range(r):
    temp = list(raw_input())
    for j in range(c):
        if temp[j] == "S":
            srow.append(i)
            scol.append(j)
    cake.append(temp)
#print cake
#print srow, scol
x, y = len(set(srow)), len(set(scol))
print (r-x)*c + (c-y)*r - (r-x)*(c-y)
'''

srow = set([])
scol = set([])
for i in range(r):
    temp = list(raw_input())
    for j in range(c):
        if temp[j] == "S":
            srow.add(i)
            scol.add(j)
x, y = len(srow), len(scol)
print (r-x)*c + (c-y)*r - (r-x)*(c-y)

