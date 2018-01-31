import random
import os


print random.randint(0,9)

arr1=[]
for i in range(0,5):
    num=random.randint(0,9)
    arr1.append(num)
print arr1



def number_game():
    num=random.randint(0,9)
    n1=1
    n2=2
    n3=3
    z=0
    k=5
    os.system('clear')
    for i in range(5):
        print "1:number==5"
        print "2:number>5"
        print "3:number<5"
        choice=int(raw_input("Enter ur choice:"))

        if (num==5 and choice==1) or (num<5 and choice==2) or (num>5 and choice==3):
            os.system('clear')
            print "congradulation u won and ur number is {} and ur choice is {}".format(num,choice)
            z+=1
            k-=1
        else:
            os.system('clear')
            print "sorry u loss ur number is {} and ur choice is {}".format(num,choice)
            k-=1
        if k==0:
            print "ur score is {} out of {}".format(z,i+1)
        else:
            print "choose again number u have {} chances".format(k)


number_game()

