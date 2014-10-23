par = map(int, raw_input().split(" "))
a = par[0]
b = par[1]

modu = 10**9 + 7

'''
if b == 1:
    print 0
else:
    total = 0
    for k in range(1, a+1):
        for denom in range(1, b):
            x = denom * k * b % modu + denom
            total += x
            if total > modu:
                total %= modu
    print total
'''

t1 = (b * (b-1)//2 )%modu
t2 = (t1 * a * (1+a)//2 * b) %modu
print (t1 + t2) % modu