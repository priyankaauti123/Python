sum=0
def is_prime_no(x):
    for i in range(2,x,1):
        if x%i==0:
            return 0
    return 1

#print prime_no(x)

def prime_fact(x):
    global prime
    for i in range(2,x,1):
        if x%i==0:
            prime=is_prime_no(i)
            if prime==1:
                print i

n1=int(raw_input("Enter no:"))
prime_fact(n1)
#prime_no(n1)

