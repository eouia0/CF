n = input()
home = []
guest = []
for i in range(n):
    par = map(int, raw_input().split(" "))
    home.append(par[0])
    guest.append(par[1])

count = 0
for i in range(n):
    for j in range(n):
        if i != j and home[i] == guest[j]:
            count += 1
print count