list_1=[5,8,3,7,9,2,1,30,4,6]

def find_max(list1):
    j=list1[0]
    for i in range(1,len(list1),1):
        if j<list1[i]:
            j=list1[i]
    return j

n=find_max(list_1)
print "max no {}".format(n)
