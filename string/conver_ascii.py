str1=input("Enter string:=")
str2=[]
str2=map(lambda x:str(ord(x)),str1)
print str2
print ', '.join(str(ord(x)) for x in str1)
