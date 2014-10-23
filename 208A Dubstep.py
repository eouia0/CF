par = raw_input()
sol = ""

i = 0
while i < len(par) and par[i:i+3] == "WUB":
    i += 3
j = len(par)-1
while j >= 0 and par[j-2:j+1] == "WUB":
    j -= 3

while i <= j:
    item = par[i:i+3]
    if item != "WUB":
        sol = sol + par[i]
        i += 1
    else:
        if sol[-1] != " ":
            sol = sol + " "
        i += 3
print sol
