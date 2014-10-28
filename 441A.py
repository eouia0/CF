#n = input()
[n, v] = map(int, raw_input().split())

seller = []
for s in range(1, n+1):
    par = map(int, raw_input().split())
    for item in par[1:]:
        if item < v:
            seller.append(s)
            break
print len(seller)
print " ".join(str(x) for x in sorted(seller))
