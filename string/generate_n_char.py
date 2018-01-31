n=int(input("Enter no:="))
ch=input("Enter character:=")

def generate_n_char(ch,n):
    str=[]
    for i in range(n):
        str.append(ch)
    print ''.join(str)

generate_n_char(ch,n)

def histogram(lst):
    for i in lst:
        generate_n_char('*',i)

list_1=[4,7,2]
histogram(list_1)

[lambda x:generate_n_char('*',x),list_1]

