#!/usr/bin/python
# -*- coding: UTF-8 -*-

def printme(str):
    print str
    return

printme("Hello Kitty")
printme("???")

def ChangeInt(a):
    a=10

b=2
ChangeInt(b)
print "123:", b

def changeme(mylist):
    mylist.append([1,2,3,4])
    print "def in value: ", mylist
    return

mylist = [10,20,30]
changeme(mylist)
print "def out value: ", mylist

printme(str = "My string")

def printinfo(arg1, *vartuple):
    print "output"
    print arg1
    for var in vartuple:
        print var
    return

printinfo(10)
printinfo(70,60,50)

sum = lambda arg1, arg2: arg1+arg2

print "After add : ", sum(10, 20)
print "After add : ", sum(20, 20)

def sum(arg1, arg2):
    total = arg1 + arg2
    print "def in :", total
    return total

total = sum(10, 20)

total = 0
def sum(arg1, arg2):
    global total # 全局变量在函数内使用，需要加gobal
    total = arg1 + arg2
    print "in value:", total
    return total

sum(10,20)
print "out value : ", total