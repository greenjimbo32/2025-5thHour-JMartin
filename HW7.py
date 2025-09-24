#Name:Jude Martin
#Class: 5th Hour
#Assignment: HW7
from stat import FILE_ATTRIBUTE_SPARSE_FILE

#1. Print Hello World!
print("hello world")

#2. Create a dictionary with 3 keys and a value for each key. One of the keys must have a value with a list containing
#three numbers inside.
bryson_info={
    "name": "bryson",
    "age": 0.0001,
    "is bryson gay": [5,32,0]
}
#3. Print the keys of the dictionary from #2.
print(bryson_info.keys())
#4. Print the values of the dictionary from #2
print(bryson_info.values())
#5. Print one of the three numbers from the list by itself
print(bryson_info["is bryson gay"][0])
#6. Using the update function, add a fourth key to the dictionary and give it a value.
bryson_info.update({"bank_acc":4})
#7. Print the entire dictionary from #2 with the updated key and value.
print(bryson_info)
#8. Make a nested dictionary with three entries containing the name of another classmate and two other pieces of information
#within each entry.
children_in_hell_hole = {
    "child_1":{
        "name": "bryson" ,
        "age":99999 ,
        "favorite_game": "rdr2",
    },
    "child_2":{
        "name": "sam" ,
        "age":0 ,
        "favorite_game": "monkey run",
    },
    "child_3":{
        "name": "brennlyn" ,
        "age":15 ,
        "favorite_game": "fortnite",
    }
}
#9. Print the names of all three classmates on the same line.
print("child_1","child_2","child_3")
#10. Use the pop function to remove one of the nested dictionaries inside and print the full dictionary from #8.
