n1=int(raw_input("Enter no:"))
sum=0
temp=n1
while temp!=0:
    rem=temp%10
    sum=sum*10+rem
    temp=temp//10

if sum==n1:
    print "palindrome"
else:
    print "not palindrome"



#by using function

n1=int(raw_input("Enter no:"))
sum=0
x=n1
def check_pal(x):
    global sum
    if x>0:
        rem=x%10
        sum=sum*10+rem
        check_pal(x//10)
    return sum

pal=check_pal(n1)
if pal==n1:
    print "palindrome"
else:
    print "not palindrome"

