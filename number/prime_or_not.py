def prime_or_not(x):
    for i in range(2,x,1):
        if x%i==0:
            print "not prime no"
            return
    print "prime no"
    return

n1=int(input("Enter no"))
prime_or_not(n1)

