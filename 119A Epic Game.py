def epic(s):
    n = s[2]
    count = 0
    while n >= 0:
        n = n - gcd(s[count%2], n)
        count += 1
    return count % 2

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a
        

s = map(int, raw_input().split(" "))
print epic(s)
