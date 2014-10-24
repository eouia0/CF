n = input()
d = map(int, raw_input().split(" "))
[s,t] = map(int, raw_input().split(" "))

if s > t:
    s, t = t, s
#print s-1, t, sum(d[s-1:t])

print min(sum(d[s-1:t-1]), sum(d[t-1:]) + sum(d[:s-1]))