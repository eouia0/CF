[n, m, k] = map(int, raw_input().split())
x = []
for i in range(m+1):
    x.append(bin(input())[2:])

ml = len(x[m])

friend = 0
for i in range(m):
    temp = x[i]
    tl = len(temp)
    count = abs(tl - ml)
    for j in range(min(tl, ml)):
        if temp[tl-1-j] != x[m][ml-1-j]:
            count += 1
    if count <= k:
        friend += 1
print friend
        