'''
par = map(int, raw_input().split(' '))

count = 0

for i in range(1, par[4]+1):
    for j in par[:4]:
    #if i % par[0] == 0 or i % par[1] == 0 or i % par[2] == 0 or i % par[3] == 0:
        if i % j == 0:
            count += 1
            break

print count
'''
l = [input() for i in range(4)]
m = input()
print(len(set([i for i in xrange(1, m+1) for j in l if i % j == 0])))