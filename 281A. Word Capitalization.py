par = raw_input()
dic = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
if not par[0] in dic:
    sol = dic[ord(par[0]) - ord("a")]
    sol = sol + par[1:]
    print sol
else:
    print par