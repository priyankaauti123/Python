n1=input("Enter n")
for i in range(n1):
    print ('*'*i)

n1=6
for i in range(n1):
    print ((n1-i)*' ')+((i-1)*'*'+(i )*'*')
for i in range(n1):
    print (i*' ')+((n1-i)*'*'+(n1-i-1)*'*')


n1=6
for i in range(n1,0,-1):
    print(n1*' '+'*'*i)


def fun2(x):
    return (x*x)

def fun3(x):
    return (2*x)

list=[3,5,7,1]
for i in list:
    print(fun3(fun2(i)))
