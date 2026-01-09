#Name:Jude Martin
#Class: 5th Hour
#Assignment: HW15

#1. import the "random" library
import random
#2. print "Hello World!"
print("hello world")
#3. Create three variables named a, b, and c, and allow the user to input an integer for each.

a=int(input("enter a number"))
b=int(input("enter a number"))
c=int(input("enter a number"))
print(a)
print(b)
print(c)
#4. Add a and b together, then divide the sum by c. Print the result.
mmm= (a + b )/c
print(mmm)
#5. Round the result from #3 up or down, and then determine if it is even or odd.
round(mmm)
if mmm % 2 == 0:
    print("even")
else:
    print("odd")

#6. Create a list of five different random integers between 1 and 10.
list=[
    random.randint(1,10),
    random.randint(1,10),
    random.randint(1,10),
    random.randint(1,10),
    random.randint(1,10),
    ]

#7. Print the 4th number in the list.
print(list[3])
#8. Append another integer to the end of the list, also random from 1 to 10.
list.append(random.randint(1,10))
#9. Sort the list from lowest to highest and then print the 4th number in the list again.
list.sort()
print(list[3])
#10. Create a while loop that starts at 1, prints i and then adds i to itself until it is greater than 100.
i = 1
while i <= 100:
    print (i)
    i += 1
#11. Create a list containing the names of five other students in the classroom.
students=["dylon","bryson","aiden","samuel","ivan"]
for student in students:
    print(student)
#12. Create a for loop that individually prints out the names of each student in the list.

#13. Create a for loop that counts from 1 to 100, but ends early if the number is a multiple of 10.

for j in range(1,101):
    if j % 10 == 0:
        break
    else:
        print(j)


#14. Free space. Do something creative. :)

i = "SIX SEVEN!!!!!!!!!!!!!!"
while i != 0:
    print (i)








