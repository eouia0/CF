#n = input()
[n,m,k] = map(int, raw_input().split(" "))
a = map(int, raw_input().split(" "))


c = 0
i = 1
for item in a:
    if item == 1:
        if m >= 1:
            m -= 1
        else:
            #print i, "m"
            c += 1
            m = 0
    elif item == 2:
        if k >= 1:
            k -= 1
        elif m >= 1:
            m -= 1
        else:
            #print i, "k"
            c += 1
            k = 0
    i += 1
print c