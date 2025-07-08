# dictionary is a python datatype which is used to store collection of items in key-value pairs. 

student={
    "name":"Praveen Singla",
    "Age":24,
    "Major":"Computer Science"}

# print(student)

# empty dictionary
my_dict={}
# print(type(my_dict))

# characterstics:
# mutable data type we can add, remove items from our dictionary
# unordered meaning that items do not have a specific order
# duplicacy is not allowed meaning keys must be unique
# finding values is really easy and quick by using dict methods

# key is a unique identifier like a name/rollno.Keys must be unique and immutable as well as keys are case-sensitive (hello, Hello)
# values is the answer to the key and this can be of any data type ex.int, float, etc.values can be duplicated and changed.

phonebook={
    "Tushar":"9898989899",
    "Vickey":"8989898996",
    "Mayank":"8989898994"
    }
# print(phonebook["Vickey"])
# using the get method
# print(phonebook.get("Mayank"))
# using the dict() constructor
empty=dict()
# print(type(empty))

person=dict(name="Golu", age=20, residence="Chandigarh")
# print(person, type(person))

# adding and updating values
phonebook={
    "Tushar":"9898989899",
    "Vickey":"8989898996",
    "Mayank":"8989898994"
    }
phonebook["Vikas"]=9352599367
# print(phonebook)

phonebook["Mayank"]=8989898986
# print(phonebook)

phonebook.update({"Tushar":7789898994})
# print(phonebook)
# del phonebook["Vikas"]
# print(phonebook)

# phonebook.clear()
# print(phonebook)
# print(type(phonebook))
# print(phonebook.keys())
# print(phonebook.values())
# print(phonebook.items())
p=phonebook.copy()
print(p)


#Q: Create two tuples 1 packed and 1 unpacked, assign them values. Now change their assigned values and also access any three elements from these tuples individually and also count occurence of a specific value in the tuple. Also find the lengths of these tuples and concatenate them and repeat the joined tuple 19 times.
