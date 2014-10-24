par = map(int, raw_input().split(" "))
n, m = par[0], par[1]
a = map(int, raw_input().split(" "))

count = 0
index = 1
for item in a:
    if index <= item:
        count += item - index
    else:
        count += n - index + item
    index = item
print count