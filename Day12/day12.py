# File handling
# Three Operations: Read, Write, Append

file = open("file_ka_naam.txt", "x")  # Open file in read mode
# x can be a, r &  w
file.close()


# Read operation
file = open("example.txt", "r")
content = file.read()
print(content)
file.close()

# Write operation
file = open("abc.txt","w")
file.write("Hello World")
file.close()

# Append Operation
file = open("abc.txt", "a")
file.write("\nThis is a new line added to the file.")
file.close()


file = open("abc.txt", "r")
file.readline()
content = file.readline()
print(content)
file.close()


file = open("abc.txt", "r")
content = file.readlines()
print(content)
file.close()

# With statement for file handling
with open("abc.txt", "r") as file:
    print(file.read())

with open("abc.txt", "r") as file:
    line = file.readlines()
    for i in line:
        print(i.strip())

with open("example.txt","w") as file:
    file.write("Hi guys\nhow are you doing?\n")


with open("abc.txt", "a") as file:
    file.write("\nThis is an appended line.\n")




# Input operation with file handling
user_name = input("Enter your name: ")
user_age = input("Enter your age: ")

with open("user_info.txt", "w") as file:
    file.write(f"Name: {user_name}\nAge: {user_age}\n")


# Remove a file
import os 
os.remove("example.txt")  # Deletes the file if it exists


# Write a program to store user input (name , age) in a file and read it back 

