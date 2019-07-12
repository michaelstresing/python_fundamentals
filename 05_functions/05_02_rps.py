'''
Code a game of rock paper scissors.

'''

# function to get hand based on number
# the function should take in a number and return the string representation of the hand

def get_hand(int):
    if int == 0:
        hand = "scissor"
    elif int == 1:
        hand = "rock"
    else:
        hand = "paper"
    return(hand)

# function should take in two hands and return a string "You won!" or "You lost :(" or "You tied!"
def determine_winner(computer, user):
    if computer == 'scissor' and user == 'rock':
        result = "You lost :("
    elif computer == 'paper' and user == 'scissor':
        result = "You lost :("
    elif computer == 'rock' and computer == 'paper':
        reulst = "You lost :("
    elif computer == user:
        result = "It was a tie!!"
    else:
        result = "You won!"
    return(result)
'''
Start here
'''

# take in a number 0-2 from the user that represents their hand
userhand = int(input("Please enter your choice, 0 = scissor, 1 = rock, 2 = paper: "))

# generate a random number 0-2 to use for the computer's hand
from random import *
computerhand = randint(0,2)

# call the function get_hand to get the string representation of the user's hand
get_hand(userhand)

# call the function get_hand to get the string representation of the computer's hand
get_hand(computerhand)

# call the function determine_winner to figure out the winner
determine_winner(computerhand, userhand)

# print out the player hand and computer hand
print(f"You chose {get_hand(userhand)}, and the computer chose {get_hand(computerhand)}.")

# print out the winner
print(determine_winner(computerhand, userhand))


