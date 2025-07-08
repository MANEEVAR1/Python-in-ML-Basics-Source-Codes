# tuples are a data type in python used for storing data in paranthesis (). It is a way of making an ordered collection of elements in python. We can store data of multiple types eg:int, str, float, char,etc...Whereas lists are mutable in python but tuples are an immmutable data type. which means that we cannot  make any changes once we create them just like strings.

tup=1,2,3,4,5
# when we store our data in tuples by using a paranthesis() this concept is called 'Tuple Packing'
print(type(tup), tup)
tup1=("rajeev",24,87.90, False)
stu=("Aman",16, 56.9, False)
str="I love Python"
tup1[0]="Vivek"
# str[2]="d"
print(str)
print(tup1)
# data consistency and integrity- which means that once a tuple is created, it cannot be altered/changed/updated.
# tuples are faster processing as compared to lists
#semantic clarity enforces the behaviour of tuple i.e immutability.
# empty tuple
tupp=()
print(type(tupp))
# tuple indexing
tup1=(24,87.90, False,"rajeev")
print(tup1[-4])
# tuple slicing
print(tup1[0:4])
# tuple length
print(len(tup1))
# tuple concetenation
tup2=tup1+tupp
print(tup2)
# tuple repetition
print(tup2*8)
#tuple membership operators
print(4 not in tup1)
# tuple operations
# 1. count-->counts the occurence of an element in our data structure.
# 2. index--> used for checking the index of a value
print(tup2.count("rajeev"))
print(tup2.index("rajeev"))
# nested tuples
tup3=(23, 56, 45,(34,98,20))
print(tup3[3][1])


#Q1:CREATE TWO LISTS OF MULTIPLE DATATYPES AND PRACTICE THE FOLLOWING FUNCTIONS ON THEM--> append, insert, extend, remove, delete & sort (DESCENDING)
#Q2: Write a program to count how many times the number 3 appears in a list.
#Q3: Create a list of 5 fruits and print the second and last fruit.
