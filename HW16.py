#Name:Jude Martin
#Class: 5th Hour
#Assignment: HW16
import random
#1. Create a def function that prints out "Hello World!"
def hello_world():
    print("hello world")
#2. Create a def function that calculates the average of three numbers (set the 3 numbers as your arguments).
def average(num1,num2,num3):
    avg = (num1 + num2 + num3) / 3
    print(avg)
#3. Create a def function with the names of 5 animals as arguments, treats it like a list, and
#prints the name of the third animal.
def animal_list(*animals):
    print("third animal", animals [2])
#4. Create a def function that loops from 1 to the number put in the argument.
def bbb(number):
    for i in range(number+1):
        print(i)
#5. Call all of the functions created in 1 - 4 with relevant arguments.
hello_world()
average(5,3,8)
animal_list("dog","cat","mouse","rat","turtle")
bbb(5)
#6. Create a variable x that has the value of 2. Print x
x=2
print(x)
#7. Create a def function that multiplies the value of 2 by a random number between 1 and 5.
def hhh():
    global x
    x = x * random.randint(1,5)
#8. Print the new value of x.
hhh()


print(x)
















