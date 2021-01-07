#Exercise-1
#Write a program to reverse a string.
str1 = input("Enter your string: ")
str2 = str1[::-1]
print(str2)

#Exercise-2
#Write a function that accepts a string and prints the
#  number of uppercase letters and lowercase letters.

str1 = input("Enter a string: ")
countUC = 0
countLC = 0
for i in str1:
    if (i.isupper()):
        countUC += 1
    elif (i.islower()):
        countLC += 1
print("Upper Case: ", countUC)
print("Upper Case: ", countLC)

#Exercise-3
#Create a function that takes a list and returns
#  a new list with unique elements of the first list
def newfunct (list1):
    myset = set()
    for x in list1:
        myset.add(x)
    print(myset)

list1 = []
n = int(input("Enter number of elements in list"))
for i in range(0,n):
    ele = int(input())
    list1.append(ele)
print(list1)
newfunct(list1)

#Exercise-4
#Write a program that accepts a hyphen-separated sequence of words as input and prints the words
#in a hyphen-separated sequence after sorting them alphabetically.

str1 = input("Enter your words: ")
for i in str1:
    items = str1.split('-')
    items.sort()
print('-', join(items))

#Exercise-5
x1 = input("Enter your string")
var1 = (lambda x: x.upper())
print (var1(x1))

#Exercise-6
def twoint():
    num1 = (input("enter first number"))
    num2 = (input("enter second number"))

    n1 = int(num1)
    n2 = int(num2)

    var1 = filter(lambda x,y: x<y
    print(var1(n1,n2))
    
twoint()

#Exercise-7
def twoint():
    num1 = input("enter first string: ")
    num2 = input("enter second string: ")

    n1 = len(num1)
    n2 = len(num2)

    var1 = (lambda n1,n2: print(num2) if (n1<n2) else(print(num1) if(n1>n2) else print(num1, num2)))
    print(var1(n1,n2))
    
twoint()

#Exercise-8
from functools import reduce
def funct():
    car1 = map(lambda x : x**2, range(1,21))
    print(tuple(car1))

funct()

#Exercise-9
def showNumbers(limit):
    for i in range(0,limit+1):
        if(i%2==0):
            print(i, "EVEN")
        else:
            print(i, "ODD")
limit = int(input("Input the limit: "))
showNumbers(limit)

#Exercise-10
var= filter(lambda x: x%2==0, range(0,21))
print(list(var))

#Exercise-11
list1= [1,2,3,4,5,6,7,8,9,10]
first = filter(lambda x: (x%2==0), list1)
second = list(first)
#print(second)
main = map(lambda x : x**2, second)
print(list(main))

#Exercise-12
def errhandling():
    try:
        z=5/0
    except:
        print("Number cannot be divided by 0")
errhandling()

#Exercise-13
#Not sure

#Exercise-14
var= filter(lambda x: x%3!=0 and x%7==0, range(0,101))
print(list(var))

#Exercise-15
n = int(input("Enter elements in list"))
ele =[]
for i in range(0,n):
    lst1 = int(input("enter list ele: "))
    mainlist = ele.append(lst1)
#print(lst)
ele2 = []
for i in range(0, mainlist):
        list2 = []
        list2 = i*i
print(list2)
#not completed

#Exercise-16
'''
def foo():
    try:
        return 1
    finally:
        return 2
k = foo()
print(k)
'''
#output : 2
'''
def a():
    try:
        f(x, 4)
    finally:
        print('after f')
        print('after f?')
a()
'''
#NameError: name 'f' is not defined