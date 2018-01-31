n1=int(raw_input("Enter no"))
rev=0
while n1>0:
    rem=n1%10
    rev=(rev*10)+rem
    print rem
    n1=n1/10

print rev
