par = map(int, raw_input().split(" "))
n, m = par[0], par[1]

for i in range(n//2, -1, -1):
    steps = i + n - 2*i
    if steps % m == 0:
        break

if steps < m:
    print -1
else:
    print steps