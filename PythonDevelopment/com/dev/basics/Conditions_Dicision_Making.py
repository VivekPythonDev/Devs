#if -else block

marks=int(input("enter marks"))

if marks<35:
    print("Re-class")
    print("hello")
else:
    print("Jump to next class")
    print("Bye")

number1=int(input("enter the number1 \t"))
number2=int(input("enter the number2 \t"))
if number1>number2:
    print("Number 1 is bigger")
else:
    print("Number 2 is bigger")

#Example if elif else

marks1=int(input("enter marks"))
if marks1<35:
    print("Grade E")
elif marks1>35 and marks1<55:
    print("Grade D")
elif marks1>55 and marks1<65:
    print("Grade C")
elif marks1>65 and marks1<85:
    print("Grade B")
elif marks1>85 and marks1<100:
    print("Grade A")
else:
    print("Invalid Input")

# Example :-Small calculator
print("1. Addtion")
print("2. Substraction")
print("3. Multiplication")
print("4. Division")
ch=int(input("Enter your choice:"))
num1=int(input("enter num1:"))
num2=int(input("enter num2:"))
if ch==1:
    print("Addition=%d"%(num1+num2))
elif ch==2:
    #%i and %d are same
    print("Substraction={}".format(num1-num2))
elif ch==3:
    print("Multilication={}".format(num1*num2))
elif ch==4:
    print("Division={}".format(num1/num2))