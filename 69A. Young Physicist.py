n = input()
force = [0 for i in range(3)]
for i in range(n):
    par = map(int, raw_input().split(" "))
    for j in range(3):
        force[j] += par[j]

flag = "YES"
for item in force:
    if item != 0:
        flag = "NO"
        break
print flag