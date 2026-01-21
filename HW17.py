#Name:Jude Martin
#Class: 5th Hour
#Assignment: HW17
import random
#1. Create a def function that plays a single round of rock, paper, scissors where the user inputs
#1 for rock, 2 for paper, or 3 for scissors and compares it to a random number generated to serve
#as the "opponent's hand".
def repeat_game():
    replay_input = input("Would you like to play again? Y/N")

    if replay_input == "Y" or replay_input == "y":
        rps()
    else:
        print("Thanks for playing!")

def rps():
    player=int(input("1 for rock, 2 for paper, or 3 for scissors"))
    opponent=random.randint(1,3)

    if player==opponent:
        print("Draw")

    #lose statements / rock - paper / paper - scissors / scissors - rock

    elif player==1 and opponent==2:
        print("You lose")
    elif player==2 and opponent==3:
        print("You lose")
    elif player==3 and opponent==1:
        print("You lose")
    elif player == 2 and opponent == 1:
        print("You win")
    elif player == 3 and opponent == 2:
        print("You win")
    elif player == 1 and opponent == 3:
        print("You win")
    repeat_game()
rps()
#2. Create a def function that prompts the user to input if they want to play another round, and
#repeats the RPS def function if they do or exits the code if they don't.



