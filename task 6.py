(Q1.) Write a program in Python to find out the character in a string which is uppercase using list comprehension.
(ANSWER:)l="MY New wORLd"
a = [i.upper() for i in l if i.isupper()]
print(a)
(OUTPUT:)['M', 'Y', 'N', 'O', 'R', 'L']
(Q2.)Write a program to construct a dictionary from the two lists containing the names of students and their corresponding subjects.
The dictionary should map the students with their respective subjects. Let’s see how to do this using for loops and dictionary comprehension.
(ANSWER:)
students = ['Smit', 'Jaya', 'Rayyan']
subjects = ['CSE', 'Networking', 'Operating System']
print("original values :"+str(students))
print("original values :"+str(subjects))
x={students[i]:subjects[i] for i in range(len(students))}
print(x)
(OUTPUT)
original values :['Smit', 'Jaya', 'Rayyan']
original values :['CSE', 'Networking', 'Operating System']
{'Smit': 'CSE', 'Jaya': 'Networking', 'Rayyan': 'Operating System'}
(Q4:)Learn More about Yield, next and Generators
(ANSWER:)
(Q5:)4. Write a program in Python using generators to reverse the string.
Input String = “Consultadd Training”
(ANSWER:)
def new_string(x):
    yield x[::-1]
rev_string=new_string("Consultadd training")
k = next(rev_string)
print(k)
or
def new_string(x):
    yield x[::-1]

for rev_string  in new_string("Consultadd training"):
    print(rev_string)
(OUTPUT)gniniart ddatlusnoC
(Q5) Write an example on decorators.
(ANSWER:)(EX1)inner functions:
def add():
    print("perform adition")
    def sub():
        print("perform subtraction")
    def mul():
        print("perform mulitplication")
add()
sub=add()
(OUTPUT:)
perform adition
perform adition
(EX2)def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")

    return wrapper

def new():
    print("this is new")

new= my_decorator(new)
print(new())





