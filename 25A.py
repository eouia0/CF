n = input()
par = map(int, raw_input().split())

i = 1
flag = True
while i < n and flag:
    d = abs(par[i-1] - par[i])
    if d % 2 != 0:
        flag = False
    i += 1

if i == n:
    print i
elif i < n and abs(par[i-1] - par[i]) % 2 != 0:
    print i
else:
    print i-1


    