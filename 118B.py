n = input() + 1
sol = []
for i in range(n):
    new = range(i) + range(i, -1, -1)
    sol.append(new)

for i in range(n-2, -1, -1):
    new = range(i) + range(i, -1, -1)
    sol.append(new)

prt = ""
for i in range(len(sol)):
    new = " ".join(str(x) for x in sol[i])
    
    new = " " *((4*n-3-len(new))//2) + new
    prt = prt + new
    if i != len(sol) - 1:
        prt = prt + "\n"

print prt