#n = map(int, raw_input().split(' '))

n = int(raw_input())

win = {}

for i in range(n):
    name = raw_input()
    if name in win:
        win[name] += 1
    else:
        win[name] = 1


print max(win, key = win.get)