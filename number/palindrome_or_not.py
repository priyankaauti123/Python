n1=int(raw_input("Enter no:"))

x=n1
sum=0
def palindrome_or_not(x):
    global sum
    global tem
    global time
    while x>0:
        rem=x%10
        time=count_digit(x)
        time=time-1
        times=tens(time)
        tem=rem+times
        sum=sum+tem
        palindrome_or_not(x//10)
    return sum


count=0
x=n1
def count_digit(x):
    global count
    while x>0:
        count=count+1
        count_digit(x//10)
    return count
x=count_digit(n1)
def tens(x):
    return (10**x)



x=count_digit(n1)
print x
print tens(x)
x=n1
pal=palindrome_or_not(x)
if pal==n1:
    print "palindrome"
else:
    print "not palindrome"

