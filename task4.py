(Q1:) Write a program to reverse a string. Sample input: “1234abcd”
mystring = input("enter string:")
backwards = mystring[::-1]
print(backwards)
(OUTPUT)
enter string:srisha
ahsirs

(Q2:)Write a function that accepts a string and prints the number of uppercase letters and lowercase letters.
(ANSWER:)
def lowup(mystring):
    j = 0
    count = 0
    for i in mystring:
        if i.islower():
            j = j + 1
        elif i.isupper():
            count = count + 1
    print("number of lowercase in character ", j)
    print("number of uppercase in charcter", count)
lowup((input("ENTER A STRING:")))
(OUTPUT:)
ENTER A STRING:SJDKHJSdskjhSKDHJKAS
number of lowercase in character  5
number of uppercase in charcter 15

(Q3.) Create a function that takes a list and returns a new list with unique elements of the first list.
(ANSWERS:)
def unique_list(first_list):
    second_list=[]
    for i in first_list:
        if i not in second_list:
            second_list.append(i)
    return second_list
print(unique_list([1,2,"siri",4,5,5,"siri"]))

(OUTPUT:)[1, 2, 'siri', 4, 5]
 
the list having unique values [1, 2, 2.4, 3, 4, 'siri']
(Q4.) Write a program that accepts a hyphen-separated sequence of words as input and prints the words
in a hyphen-separated sequence after sorting them alphabetically.
 (ANSWER:)
y=input("enter string")
x=[n for n in y.split('-')]
x.sort()
print("sorted:")
print('-'.join(x))
(outpit:)
apple-raw-book
sorted:
apple-book-raw

(Q5.) Write a program that accepts a sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
x = input("Enter String: ")
count = 0
j = 0

for i in x:
    if i.islower():
        print(i.upper())
        count = count + 1

    elif i.isupper():
        print(i.upper())
        j = j + 1
  (OUTPUT:)Enter String: this is me
T
H
I
S
I
S
M
E


(Q6.)Define a function that can receive two integral numbers in string form and compute their sum and print it in the console.
(ANSWER:)
def add(first,second):
     sum=int(first)+int(second)
     return sum
print(add(20,30))
(OUTPUT:)50
(Q7.) Define a function that can accept two strings as input and print the string with the maximum length in the console. If two strings have the same length, then the function should print both the strings line by line.
(ANSWER:)def strings(fstring, lstring):
    len_string1 = len(fstring)
    len_string2 = len(lstring)
    output = ""
    if len_string1 == len_string2:
        output = fstring + '\n' + lstring
    elif len_string1 >= len_string2:
        output = fstring
    elif len_string1 <= len_string2:
        output = lstring
    return output
print(strings("siri", "siri"))
(OUTPUT:)
A)siri
siri
(Q8:)Define a function which can generate and print a tuple where the values are square of numbers between 1 and 20 (both 1 and 20 included).
(ANSWER:)
def squaretuple():
    l = list()
    for i in range(1, 21):
        l.append(i ** 2)
    return tuple(l)

l = squaretuple()
print(l)
(OUTPUT)(1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400)


(Q9:) Write a function called showNumbers that takes a parameter called limit. It should print all the numbers between 0 and limit with a label to identify the even and odd numbers.
(ANSWER:)
def showNumbers(limit):
    for i in range(limit+1):
        if i%2==0:
            print("{0}  Even".format(i))
        else:
            print("{0}  odd".format(i))
    return
showNumbers(3)
(OUTPUT:)
0  Even
1  odd
2  Even
3  odd
(Q10:)10. Write a program which uses filter() to make a list whose elements are even numbers between 1 and 20 (both included)
(ANSWER:)
x=filter(lambda x:x%2==0,range(0,21))
print(list(x))
(OUTPUT:)[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
(Q11:)Write a program which uses map() and filter() to make a list whose elements are squares of even numbers in [1,2,3,4,5,6,7,8,9,10].
(ANSWER:)
new=[1,2,3,4,5,6,7,8,9,10]
x=map(lambda a:a**2,filter (lambda a:a%2==0,new))
print(list(x))
(OUTPUT:)
[4, 16, 36, 64, 100]
(Q12:)Write a function to compute 5/0 and use try/except to catch the exceptions
(ANSWER:)def div():
    return 5/0
    try:div()
    except ZeroDivisionError :
        print ("ZeroDivisionError")

(OUTPUT:)Process finished with exit code 0
(Q13.) Flatten the list [1,2,3,4,5,6,7] into 1234567 using reduce().
(ANSWER:)from functools import reduce
x = reduce(lambda x,y:10*x+y,[1,2,3,4,5,6,7])
print(x)
(OUTPUT:)1234567
(Q14)14. Write a program in Python to find the values which are not divisible by 3 but are a multiple of 7.
Make sure to use only higher order functions.
(ANSWER:)
li = range(30)
x = filter(lambda a: a % 3 != 0 and a % 7 == 0, li)
print(list(x))
(OUTPUT)[7, 14, 28]
(Q15.)Write a program in Python to multiply the elements of a list by itself using a traditional function and pass the function to map() to complete the operation.
(ANSWER:)
l = [1, 3, 4]
k = []
for i in l:
    k = i * i
    print(k)
new_var=map(lambda k:k*k,l)
print(list(new_var))

(OUTPUT)
1
9
16
[1, 9, 16]

(Q16)(I)
def foo():
    try:
        return 1

    finally:
        return 2
    k=foo()
    print(k)
(OUTPUT)
Process finished with exit code 0(no error because of infinite loop)
(II)
def a():
    try:
        f(x, 4)
    finally:
            print('after f')
            print('after f?') 
    a()

(OUTPUT:)  
f(x, 4)
NameError: name 'f' is not defined.










