par = map(int, raw_input().split(' '))
n = par[0]

coin = map(int, raw_input().split(' '))
coin = sorted(coin, reverse = True)

left = sum(coin)
now = 0

for i in range(len(coin)):
    now += coin[i]
    left -= coin[i]
    #print i, now, left
    if now > left:
        print (i+1)
        break