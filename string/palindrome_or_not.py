
#check palindrome
str1=input("Enter string:")
str2=str1[::-1]
print str2

if str1==str2:
    print "palindrome"
else:
    print "not palindrome"

#count no of cahracter
j=0
for i in str1:
    j=j+1
print j

#reverse string
str3=str1[::-1]
for i in str3:
    print i
