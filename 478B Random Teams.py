par = map(int, raw_input().split(' '))

people = par[0]
group = par[1]

left = people - group
kmax = (left+1)*left/2
a = left / group
b = left % group
kmin = (a+1) * a / 2 * (group - b) + (a+2) * (a+1)/2 * b
print kmin, kmax
