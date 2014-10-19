par = map(int, raw_input().split(" "))
n = par[0]
m = par[1]
day = 1

flag = True
while flag:
    n -= 1
    day += 1
    if n == 0:
        flag = False
    if day % m == 0:
        n += 1
    
print day - 1
