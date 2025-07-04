name="hardik"
# print(type(name))
# print("this is our 4th day of python course")

# indexing lets you accesss individual characters from a string or text piece.
# python follows 0 based indexing which means that it starts its counting from 0 while counting element length.
print(name[1])
# specific character extraction in a string
# helps yo extract first and last values in a string

# slicing helps you in extracting substrings from a larget string you need to specify start, stop, step
# Advay K
#stop value is always taken as stopvalue(given)-1 on the backend
# step value is the jump value that how much we want to jump between characters.
name2="Tanushree Khandelwal"
print(name2[0:])
# if step value is not given it is set to 1 by default, if start value is not given then it is taken as 0th index by default and if stop value is also not given it is taken as the last element's index value(end of the string).
str="this is a string"
print(len(str))
print(len(name2))
# concatenation means to join two different strings
name1="Maneev Arora"
name2="Himank Vaid"
name_com=name1+" "+name2
print(name_com)
# repetition means to repeat any character/string multiple number of times
# asterisk
a="h "
print(a*5)
text="Thisisatextpiece"
# lower()
print(text.upper())
print(text.lower())
# print(text.strip())
b=text.strip()
print(len(b))
print(text.replace('TEXT', 'are'))
print(text.count('a'))
print(text.find('t'))
# find returns you the index value of the passed agrument.
# -1 signifies that a value does not exist
print(text.startswith('a'))
print(text.endswith(' '))
print(text.isalnum())
print(text.isalpha())
print(text)
# isalnum() checks that if your string contains a mix of numerics and alphabets (without space).
