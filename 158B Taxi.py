n = int(raw_input())
s = map(int, raw_input().split(' '))
dic = [0] * 5

for i in s:
    dic[i] += 1

taxi = dic[4] + dic[2] // 2 + dic[3]

dic[1] -= dic[3]
if dic[2] % 2 == 1:
    taxi += 1
    dic[1] -= 2
    
if dic[1] > 0:
    taxi += (dic[1]+3)//4

print taxi
