n = input()
count = n
for i in range(1, n):
    count += (n-i) * i
print count