#Name:Jude Martin
#Class: 5th Hour
#Assignment: HW8

import random

#1. Print "Hello World!"
print("hello World!!!!!!!!!!!!!!!!!")
#2. Create 3 variables that each randomly generate a number between 1 and 10, named A, B, and C.
a=random.randint(1,10)
b=random.randint(1,10)
c=random.randint(1,10)
#3. Print A, B, and C on the same line.
print(a,b,c)
#4. Make an if statement that prints if variable A is greater than, less than, or equal to 5.
if a > 5:
        print("a is greater than 5")
elif a < 5:
        print("a is less than 5")
else:
        print("a is greater than or equal to 5")
#5. Make an if statement that prints if variable B is between 3 and 7, or not.
if b < 7 and b > 3:
    print("b is in between 7 and 3")
#6. Make an if statement that prints if variable C is even or odd.
if c % 2 == 0:
    print("c is even")
else:
    print("c is odd")
#7. Create a variable whose value is 3 + a randomly generated number between 1 and 20
jake=3+random.randint(1,20)
print(jake)
#8. Make an if statement that prints if the variable from #7 is greater than, less than, or equal to A + B + C.
if jake > a+b+c:
    print(f"{jake} is greater than a+b+c")
elif jake < a+b+c:
    print(f"{jake} is less than a+b+c")
else:
        print(f"{jake} is equal to a+b+c")