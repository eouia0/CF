par = map(int, raw_input().split(" "))
n, k = par[0], par[1]

tower = map(int, raw_input().split(" "))
record = []

remain = sum(tower) % n
divide = sum(tower) // n
#perfect = [(divide + 1) for i in range(remain)] + [divide for i in range(n-remain)]
#print perfect

def perfect(count, n, remain, divide):
    for item in count:
        if item == divide +1:
            if count[item] != remain:
                return False
        elif item == divide:
            if count[item] != n-remain:
                return False
        elif item != divide and item != divide + 1:
            if count[item] != 0:
                return False
    return True
    
count = {}
for i in tower:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

for operation in range(k):
    if not perfect(count, n, remain, divide):
        highest = tower.index(max(tower))
        lowest = tower.index(min(tower))
    
        count[tower[highest]] -=1
        if tower[highest]-1 in count:
            count[tower[highest]-1] +=1
        else:
            count[tower[highest]-1] = 1
        count[tower[lowest]] -=1
        if tower[lowest]+1 in count:
            count[tower[lowest]+1] +=1
        else:
            count[tower[lowest]+1] =1
        
        tower[highest] -= 1
        tower[lowest] += 1

        record.append(str(highest+1) + " " + str(lowest+1))
    

print max(tower) - min(tower), len(record)
for item in record:
    print item

