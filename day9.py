# set is a data type used for storing collection of unique items. Sets do not accept any duplicate item.
colors={"red", "green", "blue","red"}
print(colors)
# lst=["red", "green", "blue","red"]
# print(lst)
# col={"mayank":9897472,
#      "vivek":3746329747}
# print(type(col))
foreign={90, "list", True, 78.45, "python"}
# print(type(foreign))
# foreign_set=set(foreign)
# print(foreign_set, type(foreign_set))
# foreign.add("orange")
# foreign.add(2)
fruits={"kiwi","apple","python"}
# foreign.update(fruits)
# fruits.discard("Python")
# fruits.remove("Python")
# print(fruits)
# pop_fruits=fruits.pop()
# print("removed item:",pop_fruits)
# print("remianing items:",fruits)
# fruits.clear()
print(fruits)
# emp_st=set()
# print(type(emp_st))
# print("kiwi" not in fruits)
# set1={1,2,3,8,4,5,6,7}
# set2={4,5,6,7,3,8,1,2}
# union of sets
# st_un=set1.union(set2)
# print(st_un)
# intersection of sets
# st_in=set1.intersection(set2)  
# print(st_in)
# difference in sets (elements which are present in set1 but not set2)
# st_diff=set1-set2
# print(st_diff)
# symmetric difference
# st_syd=set1^set2
# print(st_syd)
# issubset() this method checks if one set is the subset of another set
# set1={1,2,3,8,4,5,6,7}
# set2={4,5,6,7}
# issuperset()
# print(set1.issuperset(set2))
# isdisjoint()
set1={1,2,3}
set2={4,5,6}
# print(set1.isdisjoint(set2))

# sets are unordered meaning that they don't have a specific order or index
# sets are unique, meaning they don't store a value twice/duplicate.
# sets are mutable in type but elements in sets must be immutable.
# mutable ka matlab hai changing property hai, immutable means it cannot be changed
# elements in set must be of hashable type meaning they must be immutable like tuple but if you add something like a lst which is mutable the element stored hence becomes unhashable and can destroy configuration of our set.


#Q1:Ask the user to enter a key (like id, name, or salary), print "Key exists" if it is in the dictionary, otherwise print "Key not found"
#Q2:Add a new key 'Course' with value 'Python' to a dictionary having 3 prior entries, then print the updated dictionary.
#Q3: Write a Python program that does the following:
"""Creates an empty dictionary named student_marks.

Adds the following key-value pairs to it:

'Alice': 85

'Bob': 92

'Charlie': 78

Ask the user to input a student’s name.

Print the marks of that student using the dictionary.

If the name doesn’t exist in the dictionary, print "Student not found."""
