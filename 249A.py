n = input()
a = map(int, raw_input().split())

dic = {25:0, 50:0, 100:0}
flag = True
for item in a:
    if item == 25:
        dic[item] += 1
    if item == 50:
        dic[item] += 1
        dic[25] -= 1
        if dic[25] < 0:
            print "NO"
            flag = False
            break
    if item == 100:
        dic[item] += 1
        if dic[50] != 0:
            dic[50] -= 1
            dic[25] -= 1
        else:
            dic[25] -= 3
        if dic[25] < 0:
            print "NO"
            flag = False
            break
if flag == True:
    print "YES"