import sys
An = ord('A')
def fromRXCY(s):
    ss = s.split("R")[1].split("C")
    row = int(ss[0])
    col = int(ss[1])
    #print "fromRXCY", row, col
    c = []
    while col > 0:
        temp = col % 26
        if temp == 0:
            c.append("Z")
        else:
            c.append(chr(temp + An -1))
        col //= 26
    c.reverse()
    return "".join(c) + str(row)

def toRXCY(s):
    col = s.rstrip("0123456789")
    row = s[len(col):]
    #print "toRXCY", row, col
    c = 0
    now = 1
    for i in xrange(len(col)-1, -1, -1):
        c += (ord(col[i]) - An + 1) * now
        now *= 26
    return "R" + row + "C" + str(c)
    
#print fromRXCY("R23C55")
#print toRXCY("BC23")


n = int(sys.stdin.readline())
for i in xrange(n):
    s = sys.stdin.readline().strip()
    #print s, s[0], s[1]
    if s[0] == "R" and s[1].isdigit():
        print fromRXCY(s)
    else:
        print toRXCY(s)
'''
n = 1
for i in xrange(n):
    s = "R23C55"
    if s[0] == "R" and s[1] in '0123456789':
        print fromRXCY(s)
    else:
        print toRXCY(s)
'''
