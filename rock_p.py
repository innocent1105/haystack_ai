import random


play = True

bot_ = 1
player_ = 1

def get_():
    decision = input("Select option : \n 1. Rock \n 2. Paper \n 3. Scissors \n")

    if(decision == 1):
        player_ = decision
        return
    elif(decision == 2):
        player_ = decision
        return
    elif(decision == 3):
        player_ = decision
        return

def option_(decision):
    if(decision == 1):
        return "rock"
    elif(decision == 2):
        return "paper"
    elif(decision == 3):
        return "scissors"


def play_():
    bot_ = random.randint(1, 3) 

    check_option = option_(player_)

    if(player_ == bot_):
        print(f"Both selected {check_option} \n")
        print("No score")
        return
    
    if(player_ == 1 and bot_ == 2):
        print("Computer won")


# def check_():
        
play_()