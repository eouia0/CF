n = input()
a = map(int, raw_input().split(" "))
count = 0
prev = 0
for item in a:
    #print prev, count
    prev = item + prev
    if prev < 0:
        count += 1
        prev = 0
print count