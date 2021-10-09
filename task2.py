(Q1.) Write a program in Python to perform the following operation:
If a number is divisible by 3 it should print “Consultadd” as a string
x = int(input("Enter a value:"))
if x % 3==0:
    print("Consultadd")
else:
    print("value is not divisable by 3")
If a number is divisible by 5 it should print “Python Training” as a string
x = int(input("Enter a value:"))
if x % 5==0:

    print("Python Training")
else:
    print("value is not divisable by 5")

If a number is divisible by both 3 and 5 it should print “Consultadd - Python Training” as a string.
x = int(input("Enter a value:"))
if x % 3==0  and x % 5==0:
    print("“Consultadd - Python Training”")
elif x % 3==0:
    print("x is divisible by 3")
elif x%5==0:
    print("x is divisible by 5")
elif x==0:
    print ("x is zero")
else:
    print("x is a negative integer")

(Q2.) Write a program in Python to perform the following operator based task: Ask user to choose the following option first:
If User Enter 1 - Addition
num1 = int(input("Enter first value :"))
num2 = int(input("Enter second value :"))
sum = num1+num2
print(sum)
If User Enter 2 - Subtraction
num1 = int(input("Enter first value :"))
num2 = int(input("Enter second value :"))
temp = num1 - num2
print(temp)
If User Enter 3 - Division
num1 = int(input("Enter first value :"))
num2 = int(input("Enter second value :"))
temp = num1 / num2
print(temp)
If User Enter 4 - Multiplication
num1 = int(input("Enter first value :"))
num2 = int(input("Enter second value :"))
temp = num1 * num2
print(temp)
If User Enter 5 - Average
num1 = int(input("Enter first value :"))
num2 = int(input("Enter second value :"))
num3 = int(input("Enter third value :"))
num4 = int(input("Enter fourth value :"))
avg = (num1 + num2 + num3 + num4)/2
print(avg)
(Q3.) Write a program in Python to implement the given flowchart:
    a = 10
b = 20
c = 30
avg = (a + b + c) / 3
print("avg=", avg)
if avg > a and avg > b and avg > c:
    print("average is higher than a,b,c")
elif avg> a and avg > b:
    print("average is higher than a ,b ,c")
elif avg >a and avg >c:
    print("avg is higher than a and c")
elif avg > b and avg > c:
    print("avg is higher than b and c")
elif avg > a:
    print("avg is just higher than a")
elif avg > b:
    print("avg is just higher than b")

elif avg > c:
    print("avg is just higher than c")
else:
    print("avg is higher than b")
    
 OUTPUT::avg= 20.0
avg is just higher than a
(Q4.) Write a program in Python to break and continue if the following cases occurs:
If user enters a negative number just break the loop and print “It’s Over”
(ANSWER):
    i=int(input("Enter value:"))
    while i<=0:
    print("its over")
    break

If user enters a positive number just continue in the loop and print “Good Going”
(ANSWER):
    x=int(input("enter value"))
    while x>=0:
    print("Good Going: ")
     continue
(Q5). Write a program in Python which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200.
(Q6).What is the output of the following code examples?
   A) x=123
   for i in x:
    print(i)
  (ANSWER):error ='int' object is not iterable
   B) i= 0
 while i < 5:
      print(i)
      i += 1
      if i == 3:
        break 
      else:
         print(“error”)
    (ANSWER):
        0
        error
        1
        error
        2
    C)count = 0
   while True:
      print(count)
      count += 1
      if count >= 5:
           Break(SHOULD HAVE MENTIONED break)
    (Q7.) Write a program that prints all the numbers from 0 to 6 except 3 and 6. Expected output: 0 1 2 4 5
    (ANSWER)
    for i in range(6):
    if i == 3:
        continue
    print(i)
(Q8.) Write a program that accepts a string as an input from the user and calculate the number of digits and letters.
(ANSWER)
x = input("enter string : ")
d=0
l=0
for i in x:
    if i.isdigit():
        d+=1
    elif i.isalpha():
        l+=1
print("letters",l)
print("digit",d)


     











    
    
