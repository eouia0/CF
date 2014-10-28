[n,m] = map(int, raw_input().split())
a = map(int, raw_input().split())
line = range(n)


while len(line) > 1:
    index = line[0]
    if a[index] <= m:
        #a[index] = 0
        line.remove(index)
    else:
        a[index] -= m
        line.remove(index)
        line.append(index)

    
print line[0]+1