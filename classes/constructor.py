class student:
    def __init__(self,rno,name):
        self.rno=rno
        self.name=name
    def display(self):
        print self.rno
        print self.name

std=student(16202,"priya")
std.display()
