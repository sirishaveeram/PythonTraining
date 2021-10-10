(Q1:)1. Write a program in Python to allow the error of syntax to be handled using exception handling
(ANSWER:)
try:
    x = input("Enter number: ")
    x = x + 1
    print(x)

except:
    print("Invalid input")
(Q2)Write a program in Python to allow the user to open a file by using the argv module. If the entered name is incorrect throw an exception and ask them to enter the name again. Make sure to use read only mode.
import sys

try:
    f = open("file3.txt",r )
    f=sys.argv[0]
except:
    print("entered file name is incorrect give correct name")
else:
    print("valid input:")

(Q3)3. Write a program to handle an error if the user entered a number more than four digits it should return “The length is too short/long !!! Please provide only four digits”
(ANSWER)try:
    x = int(input("Enter four digit number: "))
    if x <= 1000:
        raise ValueError
except ValueError:
    print("The length is too short/long  Please provide only four digits")
 (Q4:)Create a login page backend to ask users to enter the username and password. Make sure to ask for a Re-Type Password and if the password is incorrect give chance to enter it again but it should not be more than 3 times.
(ANSWER:)
(Q6:) Read doc.txt file using Python File handling concept and return only the even length string from the file. Consider the content of doc.txt as given below:
Hello I am a file
(ANSWER:)
f=open("doc.txt")
print(f.read(5))
print(f.read(3))
print(f.read(2))
print(f.read(3))
print(f.read(4))
f.close()
output:
    Hello
 I 
am
 a 
file

 
