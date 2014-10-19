par = map(int, raw_input().split(' '))

n = par[0]
w = par[1]
h = par[2]

env = {}
for i in range(n):
    env[i] = map(int, raw_input().split(' '))
    
env = sorted(env.items(), key = lambda x: x[1][0])

#print env

i = 0
while i < n and (env[i][1][0] <= w or env[i][1][1] <= h):
    i += 1

if i == n:
    print 0
else:
    sol = [env[i][0]+1]
    prev = env[i][1]
    i += 1
    while i < n:
        if env[i][1][0] > prev[0] and env[i][1][1] > prev[1]:
            sol.append(env[i][0]+1)
            prev = env[i][1]
        i += 1
        
    print len(sol)
    p = ""
    for i in range(len(sol)):
        p = p + str(sol[i])
        if i != len(sol) - 1:
            p = p + " "
        else:
            print p

        
        