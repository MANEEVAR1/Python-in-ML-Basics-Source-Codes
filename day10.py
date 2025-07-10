# loops are meant for prevention against repetition of a single code block multiple times
# loops are also helpful in saving time
# automation is provided through loops
# we have 2 types of loops in python: 1. For loop, 2. While loop
# for loops are used when we know about the number of iterations that how many times our code/program will work/ iterate/ repeat
# while loops are used when we don't know about the number of iterations that how many times our code/program will work/ iterate/ repeat. It will work until the condition is met and claimed false.
print("Hey Buddy")
a="I am Sorry Ma'am"
for i in range(100):
    print(a)
# range basically creates a sequence of numbers
for i in range(1,11,1):
    print(i)
a='India'
for i in a:
    print(i)

lst=["BMW", "MERCEDES", "LAMBORGHINI"]
for cars in lst:
    print(cars)

    # using a tuple instead of a list
lst=("BMW", "MERCEDES", "LAMBORGHINI")
for cars in lst:
    print(cars)

# print all even numbers between 1 and 20
for i in range(1,21):
    if i%2==0:
        print(i,"is even")

lst1=["mascara", "earrings", "hairband"]
for shl in lst1:
    print(shl)

# rule no.1--> indentation is very important because it leads to appropriate outcomes and improves understanding that the specific code/condition follws the logic in for loop
# rule no.2--> variables names must be easy, meaningful and short
# range function has 3 values start, stop and step starts from 1 by default,stops at the end of the data structure by default and step means the number of jumps between the values. Jitni bhi value denge argument mein usse ek kaam tak hi iteration hogi

# while loop
i=1
while i<10:
    i+=1
    print(i)

password=""
while password!="mani123":
    password=input("Enter Password:")
    if password!="mani123":
        print("Wrong Password, Try Again!")
    else:
        print("Access Granted")
