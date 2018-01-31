#1)square of a no
n1=int(raw_input("Enter no:"))
def square_fun(x):
    "squre of number"
   # print x*x
    n2=x*x
    return n2

#calling function
print square_fun(n1)



#2)print string

n1=raw_input("Enter string")
def print_string(x):
    "string print"
    print n1
    return

#calling function
print_string(n1)


#3)average of x and y

def average_x_y(x,y):
    return ((x+y)/2)

print "average of x and y:",float(average_x_y(4.0,5.0))


#4)lambda function

print (lambda x: (x*x)(2))


