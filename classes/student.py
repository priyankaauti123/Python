def count(arr):
    global cnt
    cnt=0
    for i in arr:
        cnt=cnt+1
    return cnt

class student:
    def accept_data(self):
        self.rno=input("enter rno:")
        self.marks=[]
        n=4
        for i in range(n):
            n1=input("Enter marks:")
            self.marks.append(n1)
    def display(self):
        print self.rno
        print self.marks
    def average(self):
        n=count(self.marks)
        global avg
        global tot
        tot=0
        for i in self.marks:
            tot=tot+i
        print tot
        avg=tot/n
        print avg

std=student()
std.accept_data()
std.display()
std.average()
