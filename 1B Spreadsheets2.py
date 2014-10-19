from string import uppercase
import sys

def fromRXCY(s):
    ss = s.split("R")[1].split("C")
    row = ss[0]
    col = int(ss[1])
    #print "fromRXCY", row, col
    #c = []
    while col > 0:
        col, d = divmod(col-1, 26)
        c.append(uppercase[d])
    c.reverse()
    print "".join(c) + row

def toRXCY(s):
    col = 0
    i = 0
    while i < len(s):
        if s[i] not in uppercase:
            row = s[i:]
            break
        col = col * 26 + uppercase.index(s[i]) + 1
        i += 1
    print "R%sC%d" %(row, col)

n = int(sys.stdin.readline())
for i in xrange(n):
    s = sys.stdin.readline().strip()
    if s[0] == "R" and s[1].isdigit():
        fromRXCY(s)
    else:
        toRXCY(s)