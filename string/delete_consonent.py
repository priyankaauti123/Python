str1=input("Enter string:=")
str2=[]
str3=[]
for x in str1:
    if x!='a' and x!='e' and x!='i' and x!='o' and x!='u':
        str2.append(x)
print ''.join(str2)
#print ''.join(str3)

