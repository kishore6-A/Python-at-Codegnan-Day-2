# add two numbers
a=6
b=12
print(a+b)

#take two numbers print quotient and reaminder
q=15
r=3
print("q=", q//r)
print("r=", q%r)

#check it is even or odd
n=int(input())
if n%2==0:
    print("even")
else:
    print("odd")

#swap two variables using arithematic operator without third variable
a=10
b=20
a=a+b
b=a-b
a=a-b
print("a=", a)
print("b=", b)

#take three largest numbers using comprasion operator

a=int(input())
b=int(input())
c=int(input())
if a>b:
    print("a is greater than")
elif b>c:
    print("b is greater than")
else:
    print("c is greater than")

#caculate the square number using power
square=int(input())
power=square**2
print(power)

#take two number check if first is divisible by second
first=int(input())
second=int(input())
if first%second==0:
    print("first is divisible by second")
else:
    print("first is not dividsible by second")

#calculate are of rectangle
length=int(input())
breadth=int(input())
area=length*breadth
print(area)

#take number print if wheather positive, negative or zero
a=int(input())
if a>0:
    print("positive")
if a<0:
    print("negative")
else:
    print("zero")

#take two numbers are equal using equality operator
a=int(input())
b=int(input())
if a==b:
    print("equal numbers")
else:
    print("not equal numbers")

#check if a person eligible for vote (>=18)
major=int(input())
if major>=18:
    print("eligible for vote")
else:
    print("not eligible for vote")

#check if it is multiple both 3 and 5

a=int(input())
if a%3==0 and a%5==0:
    print("both divisible by 3 and 5")
else:
    print("both not divisible by 3 and 5")

#greatest three numbers using nested if
a=int(input())
b=int(input())
c=int(input())
if a>b:
    if a>c:
        print("a is greater")
    else:
        print("c is greater")
else:
    if b>c:
        print("b is greater")
    else:
        print("c is greater")

#take a input marks and grade
marks=int(input())
if marks>=90:
    print("A")
if marks>=75 and marks<=89:
    print("B")
elif marks>50 and marks<=74:
    print("C")
else:
    print("Fail")
            

    

    

