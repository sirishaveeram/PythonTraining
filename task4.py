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
(Q8:)
(Q9:) Write a function called showNumbers that takes a parameter called limit. It should print all the numbers between 0 and limit with a label to identify the even and odd numbers.
(ANSWER:)def showNumbers(limit):
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







n


