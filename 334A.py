#par = map(int, raw_input().split(" "))
#n, m, a, b = par[0], par[1], par[2], par[3]

n = input()

for i in range(n):
    sol = ""
    k = 0
    for j in range(i+1, n+1) + range(1, i+1):
        sol = sol + str(k*n + j) + " "
        k += 1
    print sol[:-1]
        
        