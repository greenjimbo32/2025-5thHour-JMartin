#Name:Jude Martin
#Class: 5th Hour
#Assignment: HW12
import random
#1. Create a while loop with variable i that counts down from 5 to 0 and then prints
#"Hello World!" at the end.
i = 5
while i <= 0:
    print (i)
    i += 1
#2. Create a while loop that prints only even numbers between 1 and 30 (HINT: modulo).

k = 1
while k <= 30:
    if k % 2 == 0:
        print (k)
    k+= 1

#3. Create a while loop that prints from 1 to 30 and continues (skips the number) if the
#number is divisible by 3.
m = 1
while m <= 30:
    if m % 3 == 0:
        m+=1
        continue
    else:
        print (m)
        m+=1

#4. Create a while loop that randomly generates a number between 1 and 6, prints the result,
#and then breaks the loop if it's a 1.
g=random.randint(1,6)
while g < 6:
    if g == 1:
        break
    print (g)
    g = random.randint(1,6)

#5. Create a while loop that asks for a number input until the user inputs the number 0.
x = int(input("insert number here:"))
while x != 0:
    print (x)
    x = int(input("insert number here:"))