par = map(int, raw_input().split(" "))
l, r = par[0], par[1]#, par[2], par[3]

def gcd(a, b):
    if b == 0:
        return a
    a,b = b, a%b
    return gcd(a,b)
    

if r-l < 2:
    print -1
else:
    a = l
    stop = False
    while a <= r-2 and not stop:
        b = a+1
        while b <= r-1 and not stop:
            c = b+1
            while c <= r and not stop:
                if gcd(a, c) != 1 and gcd(a, b) == 1 and gcd(b, c) == 1:
                    stop = True
                else:
                    c += 1
            b += 1
        a += 1
    if stop == True:
        print a-1, b-1, c
    else:
        print -1
    
        
