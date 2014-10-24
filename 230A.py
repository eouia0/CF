#n = input()
[s,n] = map(int, raw_input().split(" "))
st = []

for i in range(n):
    st.append(map(int, raw_input().split(" ")))
st.sort(key = lambda x:x[0])
#print st

flag = 0
for item in st:
    if s <= item[0]:
        flag = 1
        break
    else:
        s += item[1]

print ["YES", "NO"][flag]