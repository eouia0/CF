n = input()
a = raw_input()
#[a,b] = map(int, raw_input().split())

lucky = "47"
flag = True
for item in a:
    if not item in lucky:
        flag = False
        break
if flag == False:
    print "NO"
else:
    a = map(int, list(a))
    #print a, sum(a[:n//2]), sum(a[n//2:])
    if sum(a[:n//2]) == sum(a[n//2:]):
        print "YES"
    else:
        print "NO" 
