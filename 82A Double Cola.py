def who(n):
    names = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]
    rep = len(names)
    n -= 1
    while n >= rep:
        n -= rep
        rep += rep
    
    return names[n//(rep//len(names))]
    
n = int(raw_input())
print who(n)