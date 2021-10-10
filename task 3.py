(Q1.) Create a list of 10 elements of four different data types like int, string, complex and float.
(ANSWERS:)
l = [1, "siri", 1 + 2j, 4.5,1,"siri",2.6,4,2+3j,10]
(Q2.)Create a list of size 5 and execute the slicing structure
(ANSWER)
p = [1, "siri", 1 + 2j, 4.5, 1]
print(p[0:3])
(output:)[1, 'siri', (1+2j)]
(Q3.) Write a program to get the sum and multiply of all the items in a given list.
(ANSWER:)
p = [2, 3, 4, 5]
sum = sum(p)
print(sum)
result = math.prod(p)
print((result))
(Q3:) Find the largest and smallest number from a given list.
(ANSWER:)
import math
l=[1,2,3,4]
sum=sum(l)
print(sum)
result=math.prod(l)
print(result)
output:10
24
(Q4:) Find the largest and smallest number from a given list.
p = [2, 3,8 ,4,10,30, 1,5]
p.sort()
print(p)
print("largest element in list: ", p[-1])
print("smallest element in list:",p[0])
(output)([1, 2, 3, 4, 5, 8, 10, 30]
largest element in list:  30
smallest element in list: 1

(Q5:)Create a new list which contains the specified numbers after removing the even numbers from a predefined list.
(ANSWER:)
         p = [2, 3, 8, 4, 10, 30, 1, 5]
p.sort()
print(p)
for x in p:
    if x % 2 != 0:
        print(x)
(OUTPUT)
         [1, 2, 3, 4, 5, 8, 10, 30]
1
3
5
(Q6:) Create a list of elements such that it contains the squares of the first and last 5 elements between 1 and30 (both included).
(Answer):
import math

p = list(range(1, 31))
print(p)
x = p[0:5]
print(x)
y = p[-5:]
print(y)
sqr = []
root = []
for i in x:
    j = i ** 2
    sqr.append(j)
print(sqr)
for k in y:
    l = k ** 2
    root.append(l)
print(root)
new = sqr + root
print(new)
(Q7:)Write a program to replace the last element in a list with another list. Sample input: [1,3,5,7,9,10], [2,4,6,8]
Expected output: [1,3,5,7,9,2,4,6,8]
(Answer:)old = [1, 3, 5, 9, 10]
new=[2,4,6,8]
add=old+new
print(add)
add.remove(10)
print(add)
(Q8:)Create a new dictionary by concatenating the following two dictionaries:
(ANSWER:)
 a = {1: 10, 2: 20}
b = {3: 30, 4: 40}
a.update(b)
print(a)
         output::{1: 10, 2: 20, 3: 30, 4: 40}
 (Q9:)Create a dictionary that contain numbers in the form(x:x*x) where x takes all the values between 1 and n(both 1 and n included).
         a={}
a[1]=1*1
print(a)
a[2]=2*2
print(a)
a[3]=3*3
print(a)
a[4]=4*4
print(a)
a[5]=5*5
print(a)
print(a.items())
 (Q10:)Write a program which accepts a sequence of comma-separated numbers from console and generates a list and a tuple which contains every number in the form of string.
  (ANSWER:)       
         
         
         
         
         
         
         
         
         
         
         
         
         
         
