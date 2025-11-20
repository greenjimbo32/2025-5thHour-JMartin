#Name: Jude Martin
#Class: 5th Hour
#Assignment: SC3

#You have been transferred to a new team working on a mobile game that allows you to dress up a
#model and rate other models in a "Project Runway" style competition.

#They want to start prototyping the rating system and are asking you to make it.
#This prototype needs to allow the user to input the number of players, let each player rate
#a single model from 1 to 5, and then give the average score of all of the ratings.

x=0

players=int(input("enter number of players: "))

for h in range(1,players+1):
    vote=int(input("enter vote here from 1-5: "))
    while vote < 1 or vote > 5:
        print("vote must bew between 1-5")
        vote=int(input("vote must be between 1-5: "))
    else:
        x+=vote
print(x/players)