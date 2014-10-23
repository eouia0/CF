n = input()
points = map(int, raw_input().split(" "))

count = 0
pmin = points[0]
pmax = points[0]

for item in points[1:]:
    if item < pmin or item > pmax:
        count += 1
    pmin = min(pmin, item)
    pmax = max(pmax, item)

print count