#Name:Jude Martin
#Class: 5th Hour
#Assignment: Scenario 1

#Scenario 1:
#You are a programmer for a fledgling game developer. Your team lead has asked you
#to create a nested dictionary containing five enemy creatures (and their properties)
#for combat testing. Additionally, the testers are asking for a way to input changes
#to the enemy's damage values for balancing, as well as having it print those changes
#to confirm they went through.

#It is up to you to decide what properties are important and the theme of the game.

villains={
    "villain_1":{
        "name":"penelope",
        "age":22,
        "weight":190,
        "height":5.9,
        "power": "gravity control",
        "damage": 80000
    },
    "villain_2": {
        "name": "bryson",
        "age": 6000,
        "weight": 160,
        "height": 10.00,
        "power": "car",
        "damage": 100
    },
    "villain_3": {
        "name": "wannie",
        "age": 14,
        "weight": 180,
        "height": 5.7,
        "power": "cancer",
        "damage": "infinite"
    },
    "villain_4": {
        "name": "statham",
        "age": 1000,
        "weight": 0.0002,
        "height": 5.9,
        "power": "im bringing sexy back WHAT!!!!!",
        "damage": 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
    },
    "villain_5": {
        "name":"paisley" ,
        "age": "14",
        "weight": 220,
        "height": 5.5,
        "power": "NO",
        "damage": 0
    },
}

villains["villain_1"]["damage"]=int(input("What is your villain's damage? "))
print(villains["villain_1"])

villains["villain_2"]["damage"]=int(input("What is your villain's damage? "))
print(villains["villain_2"])

villains["villain_3"]["damage"]=int(input("What is your villain's damage? "))
print(villains["villain_3"])

villains["villain_4"]["damage"]=int(input("What is your villain's damage? "))
print(villains["villain_4"])

villains["villain_5"]["damage"]=int(input("What is your villain's damage? "))
print(villains["villain_5"])


