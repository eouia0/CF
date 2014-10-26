dic = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def fromRXCY(s):
    [R,C] = s.split("C")
    sol = ""
    c = int(C)
    while c != 0:
        temp = c % 26 - 1
        if temp == -1:
            temp = 25
        sol = dic[temp] + sol
        c = c // 26
    
    return sol + R

def toRXCY(s):
    c = 0
    r = ""
    for i in range(len(s)):
        if not s[i].isdigit():
            c = 26*c + ord(s[i]) - ord("A")+1
        else:
            break
    
    return "R"+s[i:]+"C"+str(c)

n = input()
for i in range(n):
    s = raw_input()
    if s[0] == "R":
        print fromRXCY(s[1:])
    else:
        print toRXCY(s)