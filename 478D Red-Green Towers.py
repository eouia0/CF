def find(r, g, height):
    
    sol = 0
    if height == 0:
        sol = 1
        
    elif r == 0 and g == 0:
        sol = 0
        
    elif r == 0:
        if (height+1)*height/2 <= g:
            sol = 1
        else:
            sol = 0
    elif g == 0:
        if (height+1)*height/2 <= r:
            sol = 1
        else:
            sol = 0
    
    else:
        if height <= r and height <= g:
            sol += find(r - height, g, height-1)
            sol += find(r, g - height, height-1)
            
        elif height <= r:
            sol += find(r - height, g, height-1)
        elif height <= g:
            sol += find(r, g - height, height-1)
        else:
            sol = 0
            
    print r, g, height, sol
    return sol
        
   

    
    
par = map(int, raw_input().split(' '))

r = par[0]
g = par[1]

h = 1
while (h+2) * (h+1) <= (r+g) * 2:
    h += 1

#print r, g, h, "\n"
print find(r, g, h)


