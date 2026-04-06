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

