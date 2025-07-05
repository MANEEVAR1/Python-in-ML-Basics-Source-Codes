# input taking in python
# conditional statements in python

name=input("Enter Your Name:")
age=int(input("Enter your age:"))
percentage=float(input("Enter your Percentage in 12th:"))
print("Hey guys! My name is",name,"and I am",age,"years old:) and I secured",percentage,"percent in 12th Class ")

# if, elif, else

per=float(input("Enter your percentage in 12th class:"))
if per>90:
    print("Grade A")
elif per>80:
    print("Grade B")
elif per>70:
    print("Grade C")
elif per>=60:
    print("Grade D")
else:
    print("Grade F")

# in python conditional statements work on the logic of true and false
# when a conditional statement gets its logic as true on a condition, it stops iterating even if there are more conditions to evaluate.

# distance based shipping fee calculator
total_order_value=float(input("Enter your total order value:"))
state=input("Enter your state:")
if state=="Haryana":
    print("You will have to pay Rs.60/- as your shipping fee")
elif state=="Punjab" or "punjab":
    print("You will have to pay Rs.160/- as your shipping fee")
elif state=="Rajasthan":
    print("You will have to pay Rs.80/- as your shipping fee")
else:
    print("Sorry, services not delivered in your region")

# maths based shipping fee calculator
total_order_value=float(input("Enter your order value:"))
shipping_fee= (20/ 100) * total_order_value
print("total shipping fee for your order is", shipping_fee)

# You have 2 strings "I am learning Python" & "Python is easier to learn as compared to Java"
# you need to:
# 1. Join these strings.
# 2. Extract any 2 substrings out of the joined string without:
# a) Usage of Stop Value
# b) Usage of Start Value
# 3. Check what happens if you set the step value as 9
# 4. From the String "Python is easier to learn as compared to Java" find the -1 index value and note your answer.
# 5. Convert each string into upper case.
# 6. Replace "Python" with "Java" and vice versa in individual strings.
