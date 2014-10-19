n = int(raw_input())
s = map(int, raw_input().split(" "))


maxI = 0
minI = 0

for i in range(1, n):
    if s[minI] >= s[i]:
        minI = i
    if s[maxI] < s[i]:
        maxI = i
change = abs(len(s)-1-minI) + abs(0-maxI)

#print maxI, minI

if maxI > minI:
    print change - 1
else:
    print change


    
