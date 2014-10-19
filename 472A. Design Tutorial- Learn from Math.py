def isComp(x):
    i = 2
    flag = True
    while i * i <= x:
        if x % i == 0:
            return True
        i += 1
    return False

n = int(raw_input())
a = n//2
b = n - n//2
flag = True
while flag:
    if a == 0 or b == n:
        flag = False
    elif isComp(a) == True and isComp(b) == True:
        flag = False
    a -= 1
    b += 1
print a+1, b-1
