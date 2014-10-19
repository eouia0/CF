import sys
dic = {}
maxV = float('-inf')
maxP = None
for i in range(int(raw_input())):
    line = sys.stdin.readline().strip().split()
    if line[0] in dic:
        dic[line[0]] += int(line[1])
    else:
        dic[line[0]] = int(line[1])
    if dic[line[0]] > maxV:
        maxV = dic[line[0]]
        maxP = line[0]
print maxP


