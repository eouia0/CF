x = raw_input()
y = raw_input()
sol = ""

for i in range(len(x)):
    if x[i] == y[i]:
        sol = sol + "0"
    else:
        sol = sol + "1"
print sol