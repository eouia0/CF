def buildlucky(l, prev, sol):
    #print l, sol
    if l == 0:
        return sol
    else:
        new = []
        for item in prev:
            new.append(item + "4")
            new.append(item + "7")
        sol = sol + new
        return buildlucky(l-1, new, sol)

def nearly(i, l):
    lucky = buildlucky(l-1, ["4", "7"], ["4", "7"])
    #print l, lucky
    for item in lucky:
        if int(i) % int(item) == 0:
            return "YES"
    return "NO"
    
par = raw_input()
lucky = "47"
l = len(par)
print nearly(int(par), l)

