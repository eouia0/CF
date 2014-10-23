par = map(int, raw_input().split(" "))
k, d = par[0], par[1]
a = map(int, raw_input().split(" "))
dp = [1] * k
nextI = [-1] * k

start = k
ans = 1
for i in range(k-1, -1, -1):
    for j in range(i+1, min(i+700, k)):
        if abs(a[j] - a[i]) >= d and dp[j] + 1 > dp[i]:
            nextI[i] = j
            dp[i] = dp[j] + 1
    if dp[i] > ans:
        ans = dp[i]
        start = i

print ans
i = start
while i != -1:
    print i+1,
    i = nextI[i]
