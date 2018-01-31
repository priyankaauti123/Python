#upper to lower
print "upper to lower"
str1=input("Enter string:")
str2=[]
#for i in str1:
str2=str1.lower()
print str2

str3=[]
str3=map(lambda x: x.lower(),str1)
print str3
str4=[]
str4=[x.lower() for x in str1]
str4=''.join(str4)
print "str4=",str4

str4=[]
for x in str1:
    str4.append(x.lower())
str4=''.join(str4)
print "str4=",str4

str5=[]
str5=''.join(str(x) for x in str1)
print "str5=",str5


#lower to upper
print "lower to upper"
str2=[]
str2=map(lambda x:x.upper(),str1)
print str2

str3=[]
for x in str1:
    str3.append(x.upper())
print str3

