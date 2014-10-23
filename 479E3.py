par = map(int, raw_input().split(" "))
n, a, b, k = par[0], par[1], par[2], par[3]
MOD = 10**9 + 7
N = 5010

total = [0 for i in range(N)]
f = [[0 for i in range(2)] for j in range(N) ] 


