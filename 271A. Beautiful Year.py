par = int(raw_input())
flag = True
now = par + 1

notfound = True

while notfound:
    notfound = False
    year = str(now)
    count = [0 for i in range(10)]
    for i in year:
        count[int(i)] += 1
        if count[int(i)] != 1:
            notfound = True
            break
    now += 1

print now-1