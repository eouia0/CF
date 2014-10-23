a = map(int, raw_input().split(" "))
n, k = a[0], a[1]
mid = (n+1)//2

if k <= mid:
    print 2*k-1
else:
    print 2*(k-mid)