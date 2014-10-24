n = input()
a = map(int, raw_input().split(" "))
a.sort()
print " ".join(str(x) for x in a)