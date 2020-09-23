class Employee:
    empCount = 0

    def __init__(self,name,salary):
        self.name = name
        self.salary =salary
        Employee.empCount +=1

    def displayCount(self):
        print "Total Employee %d" % Employee.empCount

    def displayEmployee(self):
        print "Name: ",self.name,", Salary: ",self.salary

class Test:
    def prt(self):
        print(self)
        print(self.__class__)

t = Test()
t.prt()

emp1 = Employee("Zara",2000)
emp2 = Employee("Manni",5000)
emp1.displayEmployee()
emp2.displayEmployee()
print "Total Employee %d" % Employee.empCount

class JustCounter:
    __secretCount=0 # 私有变量
    publicCount = 0 # 公开变量

    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print self.__secretCount

counter =JustCounter()
counter.count()
counter.count()
print counter.publicCount
print counter.__secretCount