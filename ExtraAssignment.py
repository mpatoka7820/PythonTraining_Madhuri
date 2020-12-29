#Exercise-1
#Create a list of given structure and get the Access list as provided below:
x=[100,200,300,400,500,[1,2,3,4,5,[10,20,30,40,50],6,7,8,9],600,700,800]
#print(x)
print(x[5][0:4])
print(x[6:8])
print(x[::-1])
print(x[5][5][0])
print(x[:0])

#Exercise-2
#. Create a list of thousand numbers using range and xrange and see the difference between each 
# other
(range(1,1000))
(list(range(1,1000)))

#Exercise-3
'''
lst = [1,2,3,4]
tup= (1,2,3,4)

print(lst[2])
tup[2]=5

TypeError: 'tuple' object does not support item assignment 
'''
#this shows that tuple is immutable and doesn't support item assigment

#Exercise-4
#Write a program in Python to iterate through the list of numbers in the range of 1,100 and print
#the number which is divisible by 3 and is a multiple of 2.

for i in range(1,100):
    if(i%3==0 and i%2==0):
        lst1= []
        lst1 = i
        print(lst1)

#Exercise-5
#Write a program in Python to reverse a string and print only the vowel alphabet if it exists in the
#string with their index.

str = input("Enter your string: ")
str1 = str[::-1]
for i in str1:
    if((i=='a') or (i=='e') or (i=='i') or (i=='o') or (i=='u')):
        print(i, str1.index(i))  
    else:
        pass

#Exercise-6
#Write a program in Python to iterate through the string “hello my name is abcde” and print the
#string which is having an even length.

str = input("Enter your string: ")
list1 = str.split()
for i in list1:
    if (len(i)%2==0):
        print(i)
    else:
        pass

#Exercise-7
#Write a program in python to print the pair of numbers whose sum is equal to the result
#number that is let's say 8.

x = [1,2,3,4,5,6,7,8,9,-1]
z =0
for i in x:
    for j in x:
        z = i+j
        if (z == 8): 
            print("Pair:",i,j)
        else:
            pass
    
#Exercise-8
#Create two lists such as even_list and odd_list
n = int(input("Enter number of elements: "))
if (n > 5):
    n = int(input("Elements should be 5 or less :"))
a = []
for i in range(1,n+1):
    b=int(input("Enter elements: "))
    a.append(b) 
lstEven= []
lstOdd= []
for i in a:
    if (i % 2 == 0):
        lstEven.append(i)
    else:  
        lstOdd.append(i)
print(lstEven)
print(lstOdd)

#Exercise-9
#Write a program to find out the occurrence of a specific character 
# from an alphanumeric string.
str = input("")

#Exercise-10
#Generate and print another tuple whose
#values are even numbers in the given tuple

a = (1,2,3,4,5,6,7,8,9,10)
list = []
for i in a:
    if i%2==0:
        list.append(i)
print(tuple(list))

