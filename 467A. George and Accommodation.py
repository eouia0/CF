n = int(raw_input())
count = 0
for i in range(n):
    s = map(int, raw_input().split(" "))
    if s[1] - s[0] >= 2:
        count += 1
print count


    
