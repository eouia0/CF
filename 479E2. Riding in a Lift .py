par = map(int, raw_input().split(" "))
n, a, b, k = par[0], par[1], par[2], par[3]
MOD = 10**9 + 7

total = 0
nextlevel = [[] for i in range(n)]


for i in range(1, n+1):
    temp = abs(i - b)
    for j in range(max(1, i-temp+1),  min(i+temp, n)):
        if j != i:
            nextlevel[i-1].append(j)

'''
d = [[0 for j in range(n)] for i in range(k)]

for j in range(n):
    d[0][j] = len(nextlevel[j]) % MOD

for i in range(n):
    print nextlevel[i], d[0][i]

for i in range(1, k-1):
    for j in range(n):
        for item in nextlevel[j]:
            d[i][j] += d[i-1][item-1]
        d[i][j] %= MOD
        #print i,j,d

count = 0
for item in nextlevel[a-1]:
    count += d[k-2][item-1]
print count % MOD
'''

d = [0 for j in range(n)]
for j in range(n):
    d[j] = len(nextlevel[j]) % MOD

for i in range(1, k):
    new = [0 for j in range(n)]
    for j in range(n):
        for item in nextlevel[j]:
            new[j] += d[item-1]
        new[j] %= MOD
    d = new

print d[a-1]
