# list is an ordered collection of items in python
# represented by square backets
# we can store multiple datatypes in our list
# mutability
# strings are immutable in nature
# indexing, slicing, append, insert, extend, update, pop, remove, delete, membership operators(in, not in), sort, copy, concatenation, repetition
lst=[1,2,3,4,5,"nidhi","ashutosh",3.14,True,["girish"]]
# print(lst)
# print(type(lst))
lst[6]="Nidhu"
# print(lst)
# print(lst[7])
# print(lst[-10])
# print(len(lst))
# print(lst[::-1])
bcolors=["blue", "black", "purple", "pink"]
# colors.append('24')
# bcolors.insert(3,"orange")
# print(bcolors)
# print(colors[1])
lcolors=["grey", "white", "yellow", "red","black","red"]
# lcolors.sort(reverse=True)
# print(lcolors)
# bcolors.extend(lcolors)
# bcolors.pop(2)
# lcolors.remove("red")
# del bcolors
# print("purple" not in bcolors)
# print("purple" in bcolors)
num=[43,56,23,1,0,78,364]
# num.sort(reverse=True)
original=[1,2,3,4,5,"Hello", "World"]
copy=original.copy()
num1=[67,89]
add=num+num1
# list concatenation
# asterisk
print(add)
print(num1*2)
# list repetition
# print(original)
# print(copy)
# print(num)
# str="I have a cute puppy"
# str[9]="m"
# print(str)
# str1="I have a soft puppy"

# Q: You need to take user input and based on those inputs, create the best investment advisor for the user. Take inputs such as name, age, income, etc. And suggest investment options based on tailored inputs. For example: If a person is 75 years old, he should plan more in Debt MF rather than Equity MF. Use best practices.
