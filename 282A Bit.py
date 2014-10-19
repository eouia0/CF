n = int(raw_input())
x = 0
for line in range(n):
    string = raw_input()
    if string[1] == "+":
        x += 1;
    else:
        x -= 1;
print x