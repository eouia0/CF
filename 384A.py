n = input()
if n % 2 == 0:
    print n//2*n
    for i in range(n//2):
        if i != n//2-1:
            print "C."* (n//2) + "\n" + ".C"*(n//2) + "\n",
        else:
            print "C."* (n//2) + "\n" + ".C"*(n//2)
else:
    print n//2*n+(n+1)//2
    for i in range(n//2):
        print "C."* (n//2) + "C\n" + ".C"*(n//2) + ".\n",
    print "C."* (n//2) + "C" 

    