par = map(int, raw_input().split(" "))
n, m = par[0], par[1]
f = map(int, raw_input().split(" "))
f.sort()
small = f[n-1] - f[0]
for i in range(1, m-n+1):
    temp = f[n-1+i] - f[i]
    if temp < small:
        small = temp
print small
