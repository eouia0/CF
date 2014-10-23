'''
n = input()
t = {}
for i in range(n):
    par = tuple(map(int, raw_input().split(" ")))
    if par in t:
        t[par] += 1
    else:
        t[par] = 1

print max(t.values())
'''
t = {}
for _ in range(input()):
    a = raw_input()
    t[a] = t.get(a,0) + 1
print max(t.values())
