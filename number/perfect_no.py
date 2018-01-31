n1=int(raw_input("Enter no"))
num1=0
for i in range(2,n1,1):
    if n1%i==0:
        num1=num1+i

if (num1+1)==n1:
    print "perfect no"
else:
    print "not perfect no"
