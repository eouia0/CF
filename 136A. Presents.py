n = int(raw_input())
p = map(int, raw_input().split(" "))

dic = {}
for i in range(n):
    dic[i+1] = p[i]

dic = sorted(dic.items(), key = lambda x:x[1])
#print dic
sol = ""
for i in dic:
    sol = sol + str(i[0]) + " "

print sol[:-1]