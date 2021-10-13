(Q1). Create three variables in a single line and assign values to them in such a manner that each one of
them belongs to a different data type.
(ANSWER): a , b , c = 10 , "siri" , 2.3
(Q2) Create a variable of type complex and swap it with another variable of type integer.
(ANSWER):
x = 1 + 2j
y = 2
temp = x
x=y
y= temp
print(x)
print(y)

output:
 2
(1+2j)

(Q3). Swap two numbers using a third variable and do the same task without using any third variable.
(ANSWER):
Swapping two numbers using third variable:
x=10
y=20
temp=x
x=y
y=temp
print(x)
print(y)
Swapping two numbers without using third variable
x= 10
y =20
x=x+y
y=x-y
x=x-y
print(x)
print(y)
(Q4). Write a program that takes input from the user and prints it using both Python 2.x and Python 3.x
Version.
(ANSWER) :
For PYTHON 2.x::
a=rawinput("enter new value :")
print(a)
For PYTHON 3.x::
a=input(" enter new value:")
print(a)
(Q5). Write a program to complete the task given below:
Ask users to enter any 2 numbers in between 1-10 , add the two numbers and keep the sum in
another variable called z. Add 30 to z and store the output in variable result and print result as the
final output.
(ANSWER) :x=int(input("enter  first value between 1 to 10 :"))
y=int(input("enter second value between 1 to 10 :"))
z=x+y
print(z)
NewVar=z+30
print(NewVar)
(Q6). Write a program to check the data type of the entered values.
(ANSWER):we can do using type()
x = 10
print(type(x)) # output is <class 'int'>
x= "siri"
print(type(x)) #output is <class 'str'>
(Q7). Create Variables using formats such as Upper CamelCase, Lower CamelCase, SnakeCase and
UPPERCASE.
ANSWER: 
temp=sirisha veeram # for uppercase
print(temp.upper())
output:
SIRISHA VEERAM
SirishaVeeram   (UpperCamel (Pascal Case))
sirishaVeeram    (lowerCamel)
snake_case       (sirisha_veeram__)

(Q8.) If one data type value is assigned to ‘a’ variable and then a different data type value is assigned to ‘a’
again. Will it change the value? If Yes then Why?
(ANSWER):
a=10
a="siri"
print(a)
output : siri
Yes the value gets replaced...beacause variable 'a' is  not memory location its just reference



