

#for simple accept and display
class employee:
    def accept(self):
        name=[]
#        name=input("Employee name:")
#        self.name=name
        self.name="priya"
#        print self.name
#        salary=input("Employee salary")
        self.salary=60000
        prof=[]
#        prof=input("Employee profession")
#        self.prof=prof
        self.prof="mcs"

    def display(self):
        print "Hello %s" %self.name
        print self.salary
        print self.prof

emp=employee()
emp.accept()
emp.display()






