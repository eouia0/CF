par = raw_input()
number = "123"
count = {}
for item in par:
    if item in count:
        count[item] += 1
    else:
        count[item] = 1
  
sol = ""
for key in number:
    if key in count:
        for i in range(count[key]):
            sol = sol + str(key) + "+"

print sol[:-1]