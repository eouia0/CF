#par = map(int, raw_input().split(" "))
#n, m = par[0], par[1]
#a = map(int, raw_input().split(" "))
n = input()
sol = ""
for i in range(n//2):
    star = (n-2*i-1)//2
    sol = sol + "*" * star + "D" * (2*i+1) + "*" * star + "\n"
    
for i in range(n//2, -1, -1):
    star = (n-2*i-1)//2
    sol = sol + "*" * star + "D" * (2*i+1) + "*" * star + "\n"

print sol[:-1]