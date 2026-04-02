"""Assignment Operator"""
a=int(input("Enter a value: "))
b=int(input("Enter b value: "))
a+=b
a=a+b
print("Addition of To Number:", a)

##############

first_number = int(input("Enter first_number value: "))
second_number = int(input("Enter second_Number value: "))
first_number -= second_number
first_number = first_number-second_number
print("Subtraction of Two Numbers:",first_number )
#
#
#
A=int(input("Enter A Number: "))
B=int(input("Enter B Number: "))
A*=B
A=A*B
print("Multiplication of Two Numbers:", A)
#
#
#
First_Number=int(input("Enter First_Number value: "))
Second_Number=int(input("Enter Second_Number value: "))
First_Number/=Second_Number
First_Number=First_Number/Second_Number
print("Division of Two Numbers:", First_Number )
#
#
#
Hi=int(input("Enter Hi value: "))
Hello=int(input("Enter Hello value: "))
Hi%=Hello
Hi=Hi%Hello
print("Modulus of Two Numbers:", Hi)
#
#
#
Offline=int(input("Enter Offline value: "))
Online=int(input("Enter Online value: "))
Offline//=Online
Offline=Offline//Online
print("Floor Division of Two NUmbers:", Offline)



"""Relational Operator"""

j=int(input("Enter j Value: "))
k=int(input("Enter k Value: "))
print("Less Than:", j<k)
print("Greater Than:", j>k)
print("Greater Than or Equal to:", j>=k)
print("Less Than or Equal to:", j<=k)
print("Not Equal:", j!=k)

#
#
#
#

"""Logical Operator"""
x=6
if x>5 and x<10:
    print("x is between 5 and 10")

#
#
x=6
if x<5 or x<10:
    print("Condition is True")

#
#
x=6
if not(x>10):
    print("x is not greater than 10")

#
#
"""Membership Operator"""
name = "Kishore"

if "K" in name:
    print("Letter found")

#
#
list1 = [10, 20, 30, 40]

if 50 not in list1:
    print("50 is not present")

"""Identify Operator"""
x = 10
y = 10

print(x is y)

#
#
x = 10
y = 20

print(x is not y)








