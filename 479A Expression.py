a = []
for i in range(3):
    a.append(input())
t = range(6)
t[0] = sum(a)
t[1] = a[0] + a[1] * a[2]
t[2] = a[0] * a[1] + a[2]
t[3] = a[0] * a[1] * a[2]
t[4] = (a[0] + a[1]) * a[2]
t[5] = a[0] * (a[1] + a[2])
print max(t)