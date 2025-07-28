
from functions import *

# actual game loop -----------------------------------------------------------------------------------------------------

print("Play Spell:Tactics ")  # welcome to the game
input("Press Start:Game ")

for _ in range(4):  # dealing cards to player/bot
    start_player()
    start_bot()

while game is True:  # loops until health of one or both players is below one
    global health_player, health_bot

    activating_afs()  # starts aggressive play script - tries to quickly kill player
    next_round()  # initiates next round

    attack()  # options for attack
    block()  # options for block
    draw()  # options for draw

    showdown("input")  # reveals all active cards
    calc()  # doing the math, calculating new health

    end_of_game()  # checks if health is at or below zero for one or both players
    from functions import game  # getting current boolean value of game
    if game is False:
        break  # ending the while loop - ending the game

    clean_up()  # taking one marker from charged cards, putting all activated cards in discard pile
    actual_drawing()  # drawing new cards
    reset()  # setting all variables to zero
    