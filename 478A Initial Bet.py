par = map(int, raw_input().split(' '))

total = sum(par)
if total % 5 == 0:
    sol = total / 5
    if sol == 0 :
        print -1 
    else:
        print sol
else:
    print -1