#a = raw_input()
[a,b] = map(int, raw_input().split())
count = [0] * 3

for i in range(1, 7):
    if abs(i-a) == abs(i-b):
        count[1] += 1
    elif abs(i-a) > abs(i-b):
        count[2] += 1
    else:
        count[0] += 1

print " ".join(str(x) for x in count)        