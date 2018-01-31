x=input("enter a no:=")
a=[3,8,10,4,7,2]
n=len(a)

def is_member(x,a):
    n=len(a)
    for i in a:
        if i==x:
            return True
    return False

if is_member(x,a)==True:
    print "present"
else:
    print "not present"


a1=[5,8,1,9,6]

def lapping(a1,a2):
    global cnt
    cnt=0
    for i in range(len(a1)):
        for j in range(0,len(a2),1):
            if a1[i]==a2[j]:
                cnt+=1
    if cnt>=2:
        return True
    else:
        return False

if lapping(a,a1)==True:
    print "true"
else:
    print "false"
