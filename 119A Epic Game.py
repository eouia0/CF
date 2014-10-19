def epic(a, b, n):
    count = 0
    while n >= 0:
        n = n - gcd(a, n)
        count += 1
    return count % 2

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a
        

s = map(int, raw_input().split(" "))
print epic(s[0], s[1], s[2])
