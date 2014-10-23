'''
def power(n):
    total = 2
    for i in range(n-1):
        total *= 2
    return total

def combine(big, small):
    total = 1
    for i in range(big, big-small, -1):
        total *= i
    for i in range(small, 0, -1):
        total /= i
    return total
'''

from math import factorial        
origin = raw_input()
recognize = raw_input()

originCount = {"+":0, "-":0}
recogCount = {"+":0, "-":0, "?":0}

for item in origin:
    originCount[item] += 1
    
for item in recognize:
    recogCount[item] += 1

count = [0, 0, 0]
count[0] = abs(originCount["+"] - recogCount["+"])
count[1] = abs(originCount["-"] - recogCount["-"])
count[2] = recogCount["?"]

#print count

if count[0] == count[1] == 0:
    print 1
elif count[0] + count[1] == count[2]:
    #print combine(count[2], count[0])/(2**count[2])
    print factorial(count[2])*1.0/(factorial(count[0])*factorial(count[1])*(2**count[2]))
else:
    print 0
