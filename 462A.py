n = input()
flag = True
a = []
for i in range(n):
    a.append(raw_input())
i, j = 0, 0
while i < n and flag:
    j = 0
    while j < n and flag:
        temp = 0
        if i+1 < n and a[i+1][j] == "o":
            temp += 1
        if i-1 >= 0 and a[i-1][j] == "o":
            temp += 1
        if j+1 < n and a[i][j+1] == "o":
            temp += 1
        if j-1 >= 0 and a[i][j-1] == "o":
            temp += 1
        if temp % 2 != 0:
            flag = False
            
        j += 1
    i += 1
    
if flag == True:
    print "YES"
else:
    print "NO"