#par = map(int, raw_input().split(" "))
#n, m = par[0], par[1]
n = input()
pq = map(int, raw_input().split(" "))[1:] + map(int, raw_input().split(" "))[1:]
if len(set(pq)) == n:
    print "I become the guy."
else:
    print "Oh, my keyboard!"