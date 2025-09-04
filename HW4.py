#Name: Jude Martin
#Class: 5th Hour
#Assignment: HW4


#1. Print Hello World!
print("hello world")
#1. Create a list with 5 strings containing 5 different names in it.
Bands_I_listen_to = ["lincin_park" , "Red_hot_chili_peppers" , "The_beetles" , "Gorillaz" , "nirvana"]
#2. Append a new name onto the Name List.
Bands_I_listen_to.append(input("insert band to listen to: "))
print(Bands_I_listen_to)
#3. Print out the 4th name on the list.
print(Bands_I_listen_to[4])
#4. Create a list with 4 different integers in it.
Brysons_child_support = [5 , 8 , 2 , 1]
print(Brysons_child_support)
#5. Insert a new integer into the 2nd spot and print the new list.
Brysons_child_support.insert(1, 9 )
print(Brysons_child_support)
#6. Sort the list from lowest to highest and print the sorted list.
Brysons_child_support.sort()
print(Brysons_child_support)
#7. Add the 1st three numbers on the sorted list together and print the sum.
Brysons_child_support_subsum = Brysons_child_support[0] + Brysons_child_support[1] + Brysons_child_support[2]
print(Brysons_child_support_subsum)
#8. Create a list with two strings, two variables, and too boolean values.
Brysons_health_insurance = [9 , 3, "haha loser", "weirdo", True, False]
print(Brysons_health_insurance)
#9. Create a print statement that asks the user to input their own index value for the list on #8.
print(Brysons_health_insurance[int(input("haha loser"))])