str1=input("Enter string:=")
print str1[::-1]

n1=0
for x in str1:
    n1=n1+1
str2=[]
for x in range((n1-1),-1,-1):
    str2.append(str1[x])
print ''.join(str2)


#using recursion
str1=input("Enter string:=")
def reverse(x):
    if x=="":
        return x
    else:
        return reverse(x[1:])+x[0]
print reverse(str1)

