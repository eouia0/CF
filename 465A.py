n = input()
cell = raw_input()

change = 0
add = 1
for item in cell:
    temp = int(item) + add
    if temp == 2:
        add = 1
        temp = 0
    else:
        add = 0
    if temp != int(item):
        change += 1
print change