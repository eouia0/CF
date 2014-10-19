n = int(raw_input())
now = 0
capacity = -1
for i in range(n):
    s = map(int, raw_input().split(' '))
    now += s[1] - s[0]
    if now > capacity:
        capacity = now
print capacity