from operator import itemgetter
n = input()
schedule = []

for i in range(n):
    schedule.append(map(int, raw_input().split(" ")))

schedule.sort(key = itemgetter(1))
schedule.sort(key = itemgetter(0))

#print schedule
ans = -1
for item in schedule:
    if ans <= item[1]:
        ans = item[1]
    else:
        ans = item[0]
print ans