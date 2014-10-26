dic = "ZABCDEFGHIJKLMNOPQRSTUVWXY"
n = input()
for _ in xrange(n):
    s = raw_input()
    if s[0] == "R" and s[1].isdigit():
        i = s.index("C")
        row = s[1:i]
        if i > 0:
            x = int(s[i+1:])
            col = ""
            while x > 0:
                col = dic[x%26] + col
                x = (x-1)//26
            
            print col + row
    else:
        col = 0
        for i in range(len(s)):
            if s[i].isdigit():
                break
            col = col*26 + ord(s[i]) - ord("A") + 1
        print "R%sC%d" %(s[i:], col)