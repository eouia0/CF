[n, k] = map(int, raw_input().split())

joy = -float("inf")
for _ in range(n):
    par = map(int, raw_input().split())
    if par[1] <= k:
        if par[0] >= joy:
            joy = par[0]
    else:
        if par[0] - (par[1]-k) >= joy:
            joy = par[0] - (par[1]-k)

print joy