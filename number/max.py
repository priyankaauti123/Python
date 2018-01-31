def max(a,b):
    if a>b:
        return a
    else:
        return b

max_no=max(6,8)
print max_no



a=int(input("enter 1 no:"))
b=int(input("enter 2 no:"))
c=int(input("enter 3 no:"))

def max_3(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c


max_no=max_3(a,b,c)
print max_no



str=input("enter string:")

def length_str(str):
    global cnt
    cnt=0
    for i in str:
        cnt+=1
    return cnt

len=length_str(str)
print len


def check_str(str):
    if length_str(str)==1:
        if str=='a' or str=='e' or str=='i' or str=='o' or str=='u':
            return True
        else:
            return False
    else:
        return False

str=input("enter character:")
if check_str(str)==True:
    print "vowel"
else:
    print "other"



def trans_roverspracket(str):
    j=0
    str1=[]
    for i in str:
        if check_str(i)!=True:
            str1.append(i)
            str1.append('o')
            str1.append(i)
        else:
            str1.append(i)

    print ''.join(str1)

str=input("enter string:")
trans_roverspracket(str)



def accept_array():
    arr1=[]
    for i in range(5):
        num=int(input("enter no:"))
        arr1.append(num)
    return arr1

def add_fun(arr):
    global cnt
    cnt=0
    for i in arr:
        cnt+=i
    return cnt

def mult_fun(array):
    global cnt
    cnt=1
    for i in array:
        cnt*=i
    return cnt

count=add_fun(accept_array())
print "addition of array:={}".format(count)
count=mult_fun(accept_array())
print "multiplication of array:={}".format(count)

def reverse(str):
    len=length_str(str)
    str2=[]
    len-=1
    for i in range(len,-1,-1):
        str2.append(str[i])
    return str2
str=input("enter string:=")
str2=reverse(str)
print ''.join(str2)
