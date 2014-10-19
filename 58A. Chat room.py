par = map(int, raw_input().split(" "))
n = par[0]
t = par[1]
children = raw_input()
for i in range(t):
    cur = 0
    new = ""
    while cur < len(children):
        if cur < len(children) - 1 and children[cur] == "B" and children[cur+1] == "G":
             new = new + "GB"
             cur += 2
        else:
            new = new + children[cur]
            cur += 1
    #print i, children, new
    children = new

print children



