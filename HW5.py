#Name: Jude Martin
#Class: 5th Hour
#Assignment: HW5


#1. Create a list with 9 different numbers inside.
nuh_uh = [ 1, 32 , 9 , 777, 16 , 81 , 999 , 3 , 23]
#2. Sort the list from highest to lowest.
nuh_uh.sort(reverse=True)
print(nuh_uh)
#3. Create an empty list.
seven_deadly_sins=[]
#4. Remove the median number from the first list and add it to the second list.
Jimmy=nuh_uh[4]
nuh_uh.pop(4)
seven_deadly_sins.append(Jimmy)
#5. Remove the first number from the first list and add it to the second list.
jake=nuh_uh[0]
nuh_uh.pop(0)
seven_deadly_sins.append(jake)
#6. Print both lists.
print(nuh_uh)
print(seven_deadly_sins)
#7. Add the two numbers in the second list together and print the result.
seven_deadly_sins_subsum = seven_deadly_sins[0] + seven_deadly_sins[1]
print(seven_deadly_sins_subsum)
#8. Move the number back to the first list (like you did in #4 and #5 but reversed).
nuh_uh.append(seven_deadly_sins_subsum)
seven_deadly_sins.pop(0)
seven_deadly_sins.pop(0)
#9. Sort the first list from lowest to highest and print it.
nuh_uh.sort()
print(nuh_uh)