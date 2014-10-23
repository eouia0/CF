guest = raw_input()
host = raw_input()
letter = raw_input()

dic1 = {}
dic2 = {}

for item in guest:
    if item in dic1:
        dic1[item] += 1
    else:
        dic1[item] = 1

for item in host:
    if item in dic1:
        dic1[item] += 1
    else:
        dic1[item] = 1
    
for item in letter:
    if item in dic2:
        dic2[item] += 1
    else:
        dic2[item] = 1

flag = True
for key in dic1.keys():
    if not key in dic2:
        flag = False
        break
    else:
        if dic2[key] != dic1[key]:
            flag = False
            break
            
for key in dic2.keys():
    if not key in dic1:
        flag = False
        break
    else:
        if dic2[key] != dic1[key]:
            flag = False
            break
            
if flag == True:
    print "YES"
else:
    print "NO"