def find(item, cumsum):
    l = 0
    r = len(cumsum)
    while l <= r:
        m = (l+r)//2
        if item == cumsum[m]:
            return m
        elif item < cumsum[m]:
            r = m - 1
        else:
            l = m + 1
    return l

n = input()
a = map(int, raw_input().split(" "))
m = input()
q = map(int, raw_input().split(" "))

cumsum = []
s = 0
for i in a:
    s += i
    cumsum.append(s)


for item in q:
    print find(item, cumsum)+1