n = input()
c = map(int, raw_input().split())
s, d = 0, 0
i, j = 0, n-1
turn = True

while i <= j:
    if c[i] >= c[j]:
        temp = c[i]
        i += 1
    else:
        temp = c[j]
        j -= 1
    if turn:
        s += temp
        turn = False
    else:
        d += temp
        turn = True

print s, d