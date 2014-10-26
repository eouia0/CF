#n = input()
[n, x]= map(int, raw_input().split(" "))
c = map(int, raw_input().split(" "))
s = abs(sum(c))
if s%x == 0:
    print s//x
else:
    print s//x+1