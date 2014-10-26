n = input()
a = map(int, raw_input().split(" "))
count = sum(a)

index = 0
sol = ""

while count > 0:
    if a[index] > 0:
        sol = sol + "P"
        a[index] -= 1
        count -= 1
    if a[index] == 0:
        goback = False
    else:
        goback = True
    
    if goback == True:
        if index - 1 >= 0:
            sol = sol + "LR"
        else:
            sol = sol + "RL"
    else:
        if index + 1 < n:
            index += 1
            sol = sol + "R"
        else:
            index -= 1
            sol = sol + "L"
    
    #print index, sol, count

print sol[:-1]