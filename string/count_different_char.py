str1=input("Enter string:=")
upr=0
lwr=0
otr=0
for x in str1:
#    global upr
 #   global lwr
 #   global otr
    if x.isupper():
        upr=upr+1
    else:
        if x.islower():
            lwr=lwr+1
        else:
            otr=otr+1
print "upper case:=",upr
print "lower case:=",lwr
print "other character:=",otr
