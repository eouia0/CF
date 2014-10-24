par = map(int, raw_input().split(" "))
n, m, a, b = par[0], par[1], par[2], par[3]

count1 = a*n
count2 = (n//m)*b + (n%m)*a
print min(a*n, (n//m)*b+(n%m)*a, (n//m)*b+b)
