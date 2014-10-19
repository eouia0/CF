par = map(int, raw_input().split(" "))
a = par[0]
b = par[1]
count = a

while a >= b:
    count += a/b
    a = a%b + a/b

print count