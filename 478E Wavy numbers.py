par = map(int, raw_input().split(' '))

n = par[0]
k = par[1]

def kthwavy(n, k, lim):
    count = 0
    now = 0
    while count < k:
        now += n
        flag = True
        if now > lim:
            return "-1"
        string = str(now)
        for i in range(1, len(string)-1):
            if int(string[i]) <= int(string[i-1]) and int(string[i]) >= int(string[i+1]):
                flag = False
                break
            if int(string[i]) >= int(string[i-1]) and int(string[i]) <= int(string[i+1]): 
                flag = False
                break
        if flag:
            #print count, now
            count += 1

    return now


lim = pow(10,14)
if n % 100 == 0:
    print -1
elif n % 10 == 0 and k >= (100/10):
    print -1
else:
    print kthwavy(n, k, lim)