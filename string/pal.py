str=input("Enter string:=")

def check_pal(str):
    n=len(str)
    n-=1
    j=0
    for i in range(n,0,-1):
        if str[i]!=str[j]:
            j+=1
            return False
        else:
            j+=1
    return True

if(check_pal(str)==True):
    print "palindrome"
else:
    print "not palindrome"

