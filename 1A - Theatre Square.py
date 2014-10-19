'''
s = raw_input().split(" ")
n = int(s[0])
m = int(s[1])
a = int(s[2])

r = n//a
c = m//a
if n % a != 0:
	r += 1
if m % a != 0:
	c += 1
print (r*c)
'''

from math import *
n, m, a = map(int, raw_input().split())
print int(ceil(n*1.0/a) * ceil(m*1.0/a))