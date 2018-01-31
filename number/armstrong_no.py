#z=1
#def power(x,y):
#    for i in range(1,y,1):
#        z=x**z
#    return z
n1=int(raw_input("Enter no"))
times=0
temp=n1
while temp>0:
    times=times+1
    temp=temp/10
sum=0
temp=n1
while temp>0:
    rem=temp%10
    sum=sum+(rem**times)
    temp=temp/10

if n1==sum:
    print "armstrong no"
else:
    print "not armstrong no"


#by usong functions

n1=int(input("Enter no:"))
times=0
temp=n1
def count_digit(temp):
    global times
    while temp>0:
        times=times+1
        temp=temp/10
    return times

temp=n1
#times=count_digit(n1)
#print times
sum=0
def armstrong_no(temp,times):
    global sum
    if temp>0:
        rem=temp%10
        sum=sum+(rem**times)
        armstrong_no(temp//10,times)
    return sum

time=count_digit(n1)
no=armstrong_no(n1,time)
if no==n1:
    print "armstrong no"
else:
    print "not armstrong no"
