num1=int(raw_input("Enter no:"))
m1=0
m2=1
n1=num1
print m1
print m2
for i in range(n1-2):
    global num
    num=m1+m2
    print num
    m1=m2
    m2=num


m1=0
m2=1
def fibbo_series(n1):
    global num
    global m1
    global m2
    if n1!=0:
        num=m1+m2
        print num
        m1=m2
        m2=num
        fibbo_series(n1-1)
    return

print "fibbo series:"
print m1
print m2
n2=num1-2
fibbo_series(n2)
