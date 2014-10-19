par = raw_input()
lucky = "47"
count = 0
for i in par:
    if i in lucky:
        count += 1

flag = True
for i in str(count):
    if not i in lucky:
        print "NO"
        flag = False
        break
        
if flag == True:
    print "YES"