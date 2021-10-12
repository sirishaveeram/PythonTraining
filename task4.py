(Q1:) Write a program to reverse a string. Sample input: “1234abcd”
mystring = input("enter string:")
backwards = mystring[::-1]
print(backwards)
(Q2:)Write a function that accepts a string and prints the number of uppercase letters and lowercase letters.
(ANSWER:)
mystring = input("enter string:")
j=0
count=0
for i in mystring:
    if i.islower():
        j=j+1
    elif i.isupper():
        count=count+1
print("number of lowercase in character ",j)
print("number of uppercase in charcter",count)
(Q3.) Create a function that takes a list and returns a new list with unique elements of the first list.
(ANSWERS:)
def new():
    l = [1, "siri",2.4,1,2,4,2.4,"siri"]
    print(l)
    l=list(set(l))
    print("the list having unique values",l)
new()






