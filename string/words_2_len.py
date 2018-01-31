array=["hello","lo","hkkjbjsb"]


def length(str):
    global cnt
    cnt=0
    for i in str:
        cnt+=1
    return cnt

def list_to_len(list1):
    list_len=[]
    for i in list1:
        n=length(i)
        list_len.append(n)
    return list_len

list1=[]
list1=list_to_len(array)
print list1


def longest_word(list1,list2):
    max=list1[0]
    j=0
    for i in range(1,length(list1),1):
        if list1[i]>max:
            max=list1[i]
            j=i
    return list2[j]

str=[]
str=longest_word(list1,array)
print str



