#matrix = [[] for i in range(5)]
iRow, iCol = 0, 0
for row in range(5):
    par = raw_input().split(" ")
    for col in range(5):
        if par[col] == "1":
            iRow = row
            iCol = col

#print iRow, iCol
print abs(2-iRow) + abs(2-iCol)


