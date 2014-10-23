b = map(int, raw_input().split(' '))
'''
table = 0

while b[0] >= 0 and b[1] >= 0 and b[2] >= 0:
    b.sort()
    print b, table
    b[2] -= 2
    b[1] -= 1
    table += 1

print b, table
if b[0] < 0 or b[2] < 0 or b[1] < 0:
    b.sort()
    b[0] += 2
    b[1] += 1
    print b
    table += min(b) - 1

print table
    
'''
b.sort()

if b[2] > 2*(b[0] + b[1]):
    print b[0] + b[1]
else:
    print sum(b) // 3