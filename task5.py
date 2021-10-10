(Q1:)1. Write a program in Python to allow the error of syntax to be handled using exception handling
(ANSWER:)
try:
    x = input("Enter number: ")
    x = x + 1
    print(x)

except:
    print("Invalid input")
(Q2)Write a program in Python to allow the user to open a file by using the argv module. If the entered name is incorrect throw an exception and ask them to enter the name again. Make sure to use read only mode.
(Q3)3. Write a program to handle an error if the user entered a number more than four digits it should return “The length is too short/long !!! Please provide only four digits”
(ANSWER)try:
    x = int(input("Enter four digit number: "))
    if x <= 1000:
        raise ValueError
except ValueError:
    print("The length is too short/long  Please provide only four digits")
    
 
