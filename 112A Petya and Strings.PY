def comp(string1, string2):
    n1, n2 = len(string1), len(string2)
    if n1 != n2:
        return "Error"
    if n1 < 0 or n1 > 100:
        return "Error"
    for i in range(n1):
        s1 = string1[i].upper()
        s2 = string2[i].upper()
            
        if ord(s1) < ord(s2):
            return -1
        elif ord(s1) > ord(s2):
            return 1
    return 0

s1 = raw_input()
s2 = raw_input()
print comp(s1, s2)