n = input()
a = map(int, raw_input().split(" "))
a.sort(reverse = True)

total = a[0] * n

for i in a[1:]:
    #print i, n
    total += i * n
    n -= 1

print total 