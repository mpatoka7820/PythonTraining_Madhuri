#Task-2
#Exercise-1

x= int(input("Enter a value:"))
if x%3==0 & x%5==0 :
    print("Consultadd-Python Training")
elif x%5==0 :
    print ("Python Training")
elif x%3==0 :
    print ("Consultadd")

#Exercise-2
x = int(input("Please select a value:\n 1:Addition\n 2:Subtraction\n 3:Division\n 4:Multiplication\n 5:Average\n"))
if(x==1) | (x==2) | (x==3) | (x==4):
    num1 = input("Enter first value")
    num2 = input("Enter second value")
elif (x==5):
    num1, num2 = input("Enter 2 numbers for average: ").split()
    print(num1, num2)
else:
    print("NEGATIVE")

#Exercise-3
a = 10
b = 20
c = 30

avg = (a + b + c)/3
print("avg=", avg)
if (avg> a) & (avg > b) & (avg > c):
    print("avg is higher that a,b,c")
elif (avg > a) & (avg> b):
    print ("avg is higher than a,b")
elif (avg>a) & (avg>c):
    print("avg is higher than a,c")
elif (avg>b and avg>c):
    print("avg is higher than b,c")
elif(avg>a):
    print("avg is just higher than a")
elif(avg>b):
    print("avg is just higher than b")
elif(avg>c):
    print("avg is just higher than c")


#Exercise-4
while True:
    number = input("Enter a number: ")
    
        val = int(number)
        if val < 0: 
            print("It's Over")
            break
        elif val > 0:
            print("good going")
            continue
    
#Exercise-5
for i in range(2000,3200):
    if (i%7==0) & (i%5==0):
        print(i)

#Exercise-6
#6.1
x=123
for i in x:
    print(i)
 #TypeError: 'int' object is not iterable

#6.2

'''
0
error
1
error
2
'''

#6.3
0
1
2
3
4

#Exercise-7

for i in range(0,6):
    if (i<6):
        if(i==3) | (i==6):
            continue
    print(i)
    i+=1
    
#Exercise-8
x = input("Enter a String: ")
number1=0
character=0
for i in x:
    if (i.isdigit()):
        number1= number1 +1
    elif(i.isalpha()):
        character=character+1
    else :
        pass
print("Numbers in String are:", number1)
print("Character in String are:", character)


#Exercise-9.1
a = 7
b= int(input("Guess the lucky number"))
while True:
    if(a==b):
        print("Congrats You guessed it")
        break
    elif (a!=b):
        print("Try again")
        continue

#Exercise-9.2
a = 7
b= int(input("Guess the lucky number"))
while True:
    if(a==b):
        print("Congrats You guessed it")
        break
    elif (a!=b):
        print("Do you want to guess again?(yes/no)?")
        answer= input()
        if(answer=='yes'):
           b= int(input("Guess the lucky number"))
           continue
        else:
            break 

#Exercise-10
a=7
i=1
while i <= 5:
    b= int(input("Guess the lucky number"))
    if(a == b):
        print("Good Guess!")
        i+=1
    elif(a!=b):
        print("Try again!")
        i+=1
    print("Game Over!")

#Exercise-11
a=7
i=1
while i <= 5:
    b= int(input("Guess the lucky number:"))
    if(a == b):
        print("Good Guess!")
        break
        i+=1
    elif(a!=b):
        print("Try again!")
        i+=1
    print("Sorry but that was not very succesful")



    




    
    