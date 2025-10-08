#Name: Jude Martin
#Class: 5th Hour
#Assignment: HW9

import random

#1. Print "Hello World!"
print("hello world!!!")
#2. Create a list with three variables that each randomly generate a number between 1 and 100
monkey= [random.randint(1,100),random.randint(1,100),random.randint(1,100),random.randint(1,100)]
print(monkey)
#3. Print the list.
print(monkey)
#4. Create an if statement that determines which of the three numbers is the highest and prints the result.
if monkey[0] > monkey[1] and monkey[0] > monkey[2]:
    print("one is bigger than number 1 and 3")
    num= monkey[0]
elif monkey[1] > monkey[0] and monkey[1] > monkey[2]:
    print("number 2 is bigger than number 3")
    num= monkey[1]
else:
    print("three is bigger than number 1 and 2")
    num= monkey[2]
#5. Tie the result (the largest number) from #4 to a variable called "num".

#6. Create a nested if statement that prints if num is divisible by 2, divisible by 3, both, or neither.
if num % 2 ==0:
    if num % 3 == 0:
        print("divisible by both")
    else:
        print("divisible by just 2")
else:
    if num % 3 == 0:
        print("divisible by just 3")
    else:
        print("it is not divisible by two or three")


