#Task- One
#Exercise1 Define variable in single line
a,b,c ='1','2.01', 'string'
print(a,b,c)

#Exercise2 Swap
a = 1 +2j
b = 3
a,b = b,a
print(a,b)

#Exercise3
x = input("Enter the first value:")
y = input("Enter the Second value:")
temp_var = x
x = y
y = temp_var
print ("Swapped Value of x is", x)
print ("Swapped value of y is", y)

#Exercise3.1
h= input("Enter first value ")
i= input("Enter Second Value ")
h, i = i, h
print(h,i)

#Exercise4
x = input("Please enter a string:")
print(x)

#Exercise5
f = int(input("Enter value between 1-10 "))
k = int(input("Enter value between 1-10 "))
z =f+k
result=z+30
print(result)

#Exercise6
a = input("Enter the variable to know the data type")
print("The data type for the variable is:"type(eval(a)))

#Exercise7
x = input("Enter your string to be converted into Upper CamelCase")

#Exercise8
#Upper CamelCase
x = input("Enter for Upper CamelCase: M")
print("Upper CamelCase", x.capitalize())

#LowerCamelCase
x = input("Enter for Lower CamelCase: ")
print("Lower CameLCase", x.lower())

#SnakeCase

#Exercise8
a = int(input("value :"))
a = float(input("Value2: "))
print(a)
print(type(a))

#Yes it will replace it with the latest value
