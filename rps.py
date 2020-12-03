from random import randint

# create an array of options
t = ["rock", "paper", "scissors"]

# assign a random play to the bot
bot = t[randint(0, 2)]

# set player to false for epic loop
player = False

while player == False:

    player = input("rock, paper, scissors? ")
    if player == bot:
        print("Tie!")
    elif player == "rock":
        if bot == "paper":
            print("You lose, noob lmao,", bot, "covers", player)
        else:
            print("You win! i guess...")
    elif player == "paper":
        if bot == "scissors":
            print("You LMAO loser!", bot, "slices", player)
        else:
            print("You win, but you got lucky")
    elif player == "scissors":
        if bot == "rock":
            print("WOW you're so bad PepeLaugh", bot, "crushes", player)
        else:
            print("bruh... gg i guess")
    else:
        print("That's not a valid play!")

# set player back to false and assign the bot another play to continue the loop!!! camro epic
    player = False
    bot = t[randint(0, 2)]
