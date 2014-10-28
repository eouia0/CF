a = raw_input()
#a = map(int, raw_input().split())

for i in range(len(a)):
    if a[i] == "0":
        break

print a[:i]+a[i+1:]