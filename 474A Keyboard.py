direction = raw_input()
if direction == "R":
    d = -1
elif direction == "L":
    d = 1
origin = raw_input()
keyboard = "qwertyuiopasdfghjkl;zxcvbnm,./"

sol = ""
for item in origin:
    #print keyboard.index(item)
    sol = sol + keyboard[keyboard.index(item)+d]

print sol