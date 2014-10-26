n = input()
now = []

for _ in range(n):
    par = raw_input()
    if par != "pwd":
        s = par[3:].split("/")
        if s[0] == "":
            now = []
        for item in s:
            if item and item != "..":
                now.append(item)
            elif item == "..":
                now.pop()          
        #print now
    else:
        sol = "/"
        for item in now:
            sol = sol + item + "/"
        print sol