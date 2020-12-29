#Task-3
#Exercise-1
#Create a list of 10 elements of four different data types like int, string, complex and float.
List =[1,2,3,"mad","cat","dog",2+4j,6+7j,7.6,8.9]
print(List)

#Exercise-2
#Create a list of size 5 and execute the slicing structure 

List1= [1,2,3,4,5]
print(List1[0:2])
print(List1[-1])
print(List1[:-1])
print(List1[-1:])
print(List1[0:5:2])

#Exercise-3
#Write a program to get the sum and multiply of all the items in a given list.

List3=[3,4,5]
List4=[7,8,9]
from functools import reduce

sum = reduce((lambda x,y: x+y), List3)
multi= reduce((lambda x,y: x*y), List4)
print(sum)
print(multi)

#Exercise-4
#Find the largest and smallest number from a given list.
List5=[5,66,7,33,9]

print(min(List5))
print(max(List5))

#Exercise-5
#Create a new list which contains the specified numbers after removing the even numbers from a

List6=[1,2,3,4,5,6,7,8,9,10]
newlist = filter((lambda x: x%2!=0), List6)
print(list(newlist))

#Exercise-6
# Create a list of elements such that it contains the squares of the first and last 5 elements between 1 and30 (both included).
sqrt = lambda x,y: [i*i for i in range(x,y)]
#print(sqrt(1,31))
list8=sqrt(1,31)
l1= list8[:5]
l2 = list8[-5:]
l3 = l1 + l2
print(l3)

#Exercise-7
#Write a program to replace the last element in a list with another list.

l1= [1,3,5,7,9,10]
l2 = [2,4,6,8]
l1.pop()
l1.extend(l2)
print(l1)

#Exercise-8
#Create a new dictionary by concatenating the following two dictionaries:

a ={1:10,2:20}
b ={3:30,4:40}

a.update(b)
print("Dictionary",a)

#Exercise-9
#Create a dictionary that contain numbers in the form(x:x*x) where x takes all the values between 1 and n(both 1 and n included)

n = int(input("Input a number: "))
d = dict()

for x in range(1,n+1):
    d[x]=x*x

print(d)

#Exercise-10
#Write a program which accepts a sequence of comma-separated numbers from console and generates a list and a tuple which contains every number in the form of string.

lis=input("From a comma-separated list of numbers get:\n a List and a Tuple:\n")

lis=lis.split(",")
tup= tuple(lis)
print(lis)
print(tup)