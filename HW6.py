#Name:Jude Martin
#Class: 5th Hour
#Assignment: HW6


#1. Import the "random" library
import random
#2. print "Hello World!"
print("hello world")
#3. Create three different variables that each randomly generate an integer between 1 and 10
jimmy_1 = random.randint(1,10)
jimmy_2 = random.randint(1,10)
jimmy_3 = random.randint(1,10)
#4. Print the three variables from #3 on the same line.
print(jimmy_1, jimmy_2, jimmy_3)
#5. Add 2 to the first variable in #3, Subtract 4 from the second variable in #3, and multiply by 1.5 the third variable in #3.
jankins = jimmy_1 + 2
jankins_2 = jimmy_2 - 4
jankins_3 = jimmy_3 * 1.5
#6. Print each result from #5 on the same line.
print(jankins, jankins_2, jankins_3)
#7. Create a list containing four variables that each randomly generate an integer between
brysons_play_station = [random.randint(1,6),random.randint(1,6),random.randint(1,6),random.randint(1,6)]
#8. Sort the list in #7 and print it.
brysons_play_station.sort()
print(brysons_play_station)
#9. Add together the highest three numbers in the list from #7 and print the result.
brysons_child_support = brysons_play_station[1] + brysons_play_station[2] + brysons_play_station[3]
print(brysons_child_support)
#10. Create a list with 5 names of other students in this class and print the list.
people_in_class = ["bryson", "jude", "brennlyn", "ivan", "dilan"]
print(people_in_class)
#11. Shuffle the list in #10 and print the list again.
random.shuffle(people_in_class)
print(people_in_class)
#12. Print a random choice from the list of names from #10
print(random.choice(people_in_class))