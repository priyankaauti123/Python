str1=[]
str3=[]
ch1=input("Enter char:=")
for i in range(3):
    str2=[]
    str2=input("Enter string:=")
    str1.append(str2)


print str3
print str1

for i in str1:
    if i[0]==ch1:
        str3.append(i)
print str3

for x in str3:
    print ''.join(x)

