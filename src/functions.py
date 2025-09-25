
from variables import *
import random
game = True


# state of game --------------------------------------------------------------------------------------------------------

def state_of_game(game):  # way to print the complete overview of the game - important control instance
    global rounds

    global hand_bot, deck_bot, discard_pile_bot, health_bot
    global attack_field_bot, block_field_bot, draw_field_bot
    global reserve_block, reserve_draw, attack_frenzy_system

    global hand_player, deck_player, discard_pile_player, health_player
    global attack_field_player, block_field_player, draw_field_player

    print(f"\nRound {rounds} \n")
    if game == 0:
        print(f"Reserve:Block           Reserve:Draw ")
        print(f"{reserve_block}                      {reserve_draw} ")
    print(f"                                                    Deck:Bot ")
    print(f"Hand:Bot                                            {(', '.join(deck_bot))} ")
    print(f"{(', '.join(hand_bot))} ")
    print(f"                                                    Discard:Bot ")
    print(f"          Draw:Bot                                  {(', '.join(discard_pile_bot))} ")

    if not draw_field_bot:  # used to figure out the state of the card in playa
        print(f"          [] \n")
    elif len(draw_field_bot) == 3:
        print(f"          {draw_field_bot[0]} [1/2] \n")
    elif len(draw_field_bot) == 2:
        print(f"          {draw_field_bot[0]} [2/2] \n")
    else:
        print(f"          {draw_field_bot[0]} [1/1] \n")

    print(f"                                                    Life:Bot ")
    print(f"Block:Bot            Attack:Bot                     {health_bot} ")

    if not block_field_bot:  # used to figure out the state of the card in play
        print(f"[]                  ", end=" ")
    elif len(block_field_bot) == 3:
        print(f"{block_field_bot[0]} [1/2]             ", end=" ")
    elif len(block_field_bot) == 2:
        print(f"{block_field_bot[0]} [2/2]             ", end=" ")
    else:
        print(f"{block_field_bot[0]} [1/1]             ", end=" ")

    if not attack_field_bot:  # used to figure out the state of the card in play
        print(f"[] \n")
    elif len(attack_field_bot) == 3:
        print(f"{attack_field_bot[0]} [1/2] \n")
    elif len(attack_field_bot) == 2:
        print(f"{attack_field_bot[0]} [2/2] \n")
    else:
        print(f"{attack_field_bot[0]} [1/1] \n")

    if attack_frenzy_system is True:
        print("----Attack:Frenzy-----System:Activated----")
    else:
        print("------------------------------------------")
    print(f"                                                    Life:Player ")
    print(f"Attack:Player        Block:Player                   {health_player} ")

    if not attack_field_player:  # used to figure out the state of the card in play
        print(f"[]                  ", end=" ")
    elif len(attack_field_player) == 3:
        print(f"{attack_field_player[0]} [1/2]             ", end=" ")
    elif len(attack_field_player) == 2:
        print(f"{attack_field_player[0]} [2/2]             ", end=" ")
    else:
        print(f"{attack_field_player[0]} [1/1]             ", end=" ")

    if not block_field_player:  # used to figure out the state of the card in play
        print(f"[] ")
    elif len(block_field_player) == 3:
        print(f"{block_field_player[0]} [1/2] ")
    elif len(block_field_player) == 2:
        print(f"{block_field_player[0]} [2/2] ")
    else:
        print(f"{block_field_player[0]} [1/1] ")

    print(f"                                                    Discard:Player ")
    print(f"          Draw:Player                               {(', '.join(discard_pile_player))} "),

    if not draw_field_player:  # used to figure out the state of the card in play
        print(f"          [] ")
    elif len(draw_field_player) == 3:
        print(f"          {draw_field_player[0]} [1/2] ")
    elif len(draw_field_player) == 2:
        print(f"          {draw_field_player[0]} [2/2] ")
    else:
        print(f"          {draw_field_player[0]} [1/1] ")

    print(f"                                                    Deck:Player ")
    print(f"Hand:Player                                         {(', '.join(deck_player))} ")
    if hand_player:
        print(f"{(', '.join(hand_player))} \n")
    else:
        print(f"{len(hand_player)} \n")


# reveal ---------------------------------------------------------------------------------------------------------------

def turn():  # printing game board in the rounds - not revealing enemy cards
    global rounds

    global hand_bot, show_hand_bot, deck_bot, discard_pile_bot, health_bot
    global attack_field_bot, block_field_bot, draw_field_bot

    global hand_player, deck_player, discard_pile_player, health_player
    global attack_field_player, block_field_player, draw_field_player

    show_hand_bot = 0
    show_hand_bot += len(hand_bot) + len(reserve_block) + len(reserve_draw)

    print(f"\nRound {rounds} ")
    print(f"                                                    Deck:Bot ")
    print(f"Hand:Bot                                            {len(deck_bot)} ")
    print(f"{show_hand_bot} ")
    print(f"                                                    Discard:Bot ")
    print(f"          Draw:Bot                                  {len(discard_pile_bot)} ")

    if not draw_field_bot:  # used to figure out the state of the card in play
        print(f"          [] ")
    elif len(draw_field_bot) == 3:
        print(f"          [1/2] ")
    elif len(draw_field_bot) == 2:
        print(f"          [2/2] ")
    else:
        print(f"          [1/1] ")

    print(f"                                                    Life:Bot ")
    print(f"Block:Bot            Attack:Bot                     {health_bot} ")

    if not block_field_bot:  # used to figure out the state of the card in play
        print(f"[]                  ", end=" ")
    elif len(block_field_bot) == 3:
        print(f"[1/2]               ", end=" ")
    elif len(block_field_bot) == 2:
        print(f"[2/2]               ", end=" ")
    else:
        print(f"[1/1]               ", end=" ")

    if not attack_field_bot:  # used to figure out the state of the card in play
        print(f"[] \n")
    elif len(attack_field_bot) == 3:
        print(f"[1/2] \n")
    elif len(attack_field_bot) == 2:
        print(f"[2/2] \n")
    else:
        print(f"[1/1] \n")

    if attack_frenzy_system is True:
        print("----Attack:Frenzy-----System:Activated----")
    else:
        print("------------------------------------------")
    print(f"                                                    Life:Player ")
    print(f"Attack:Player        Block:Player                   {health_player} ")

    if not attack_field_player:  # used to figure out the state of the card in play
        print(f"[]                  ", end=" ")
    elif len(attack_field_player) == 3:
        print(f"{attack_field_player[0]} [1/2]             ", end=" ")
    elif len(attack_field_player) == 2:
        print(f"{attack_field_player[0]} [2/2]             ", end=" ")
    else:
        print(f"{attack_field_player[0]} [1/1]             ", end=" ")

    if not block_field_player:  # used to figure out the state of the card in play
        print(f"[] ")
    elif len(block_field_player) == 3:
        print(f"{block_field_player[0]} [1/2] ")
    elif len(block_field_player) == 2:
        print(f"{block_field_player[0]} [2/2] ")
    else:
        print(f"{block_field_player[0]} [1/1] ")

    print(f"                                                    Discard:Player ")
    print(f"          Draw:Player                               {len(discard_pile_player)} ")

    if not draw_field_player:  # used to figure out the state of the card in play
        print(f"          [] ")
    elif len(draw_field_player) == 3:
        print(f"          {draw_field_player[0]} [1/2] ")
    elif len(draw_field_player) == 2:
        print(f"          {draw_field_player[0]} [2/2] ")
    else:
        print(f"          {draw_field_player[0]} [1/1] ")

    print(f"                                                    Deck:Player ")
    print(f"Hand:Player                                         {len(deck_player)} ")
    if hand_player:
        print(f"{(', '.join(hand_player))} \n")
    else:
        print(f"{len(hand_player)} \n")

# showdown -------------------------------------------------------------------------------------------------------------

def showdown(skip):  # prints game board, reveals all cards that are active in the given round
    global rounds

    global hand_bot, show_hand_bot, deck_bot, discard_pile_bot, health_bot
    global attack_field_bot, block_field_bot, draw_field_bot

    global hand_player, deck_player, discard_pile_player, health_player
    global attack_field_player, block_field_player, draw_field_player

    show_hand_bot = 0
    show_hand_bot += len(hand_bot) + len(reserve_block) + len(reserve_draw)

    if skip == "input":
        input(f"\nPress:Showdown ")
    else:
        pass
    print(f"\nRound {rounds} ")
    print(f"                                                    Deck:Bot ")
    print(f"Hand:Bot                                            {len(deck_bot)} ")
    print(f"{show_hand_bot} ")
    print(f"                                                    Discard:Bot ")
    print(f"          Draw:Bot                                  {len(discard_pile_bot)} ")

    if not draw_field_bot:  # used to figure out the state of the card in play
        print(f"          [] \n")
    elif len(draw_field_bot) == 3:
        print(f"          [1/2] \n")
    elif len(draw_field_bot) == 2:
        print(f"          {draw_field_bot[0]} [2/2] \n")
    else:
        print(f"          {draw_field_bot[0]} [1/1] \n")

    print(f"                                                    Life:Bot ")
    print(f"Block:Bot            Attack:Bot                     {health_bot} ")

    if not block_field_bot:  # used to figure out the state of the card in play
        print(f"[]                  ", end=" ")
    elif len(block_field_bot) == 3:
        print(f"[1/2]               ", end=" ")
    elif len(block_field_bot) == 2:
        print(f"{block_field_bot[0]} [2/2]             ", end=" ")
    else:
        print(f"{block_field_bot[0]} [1/1]             ", end=" ")

    if not attack_field_bot:  # used to figure out the state of the card in play
        print(f"[] \n")
    elif len(attack_field_bot) == 3:
        print(f"[1/2] \n")
    elif len(attack_field_bot) == 2:
        print(f"{attack_field_bot[0]} [2/2] \n")
    else:
        print(f"{attack_field_bot[0]} [1/1] \n")

    if attack_frenzy_system is True:
        print("----Attack:Frenzy-----System:Activated----")
    else:
        print("------------------------------------------")
    print(f"                                                    Life:Player ")
    print(f"Attack:Player        Block:Player                   {health_player} ")

    if not attack_field_player:  # used to figure out the state of the card in play
        print(f"[]                  ", end=" ")
    elif len(attack_field_player) == 3:
        print(f"[1/2]               ", end=" ")
    elif len(attack_field_player) == 2:
        print(f"{attack_field_player[0]} [2/2]             ", end=" ")
    else:
        print(f"{attack_field_player[0]} [1/1]             ", end=" ")

    if not block_field_player:  # used to figure out the state of the card in play
        print(f"[] \n")
    elif len(block_field_player) == 3:
        print(f"[1/2] \n")
    elif len(block_field_player) == 2:
        print(f"{block_field_player[0]} [2/2] \n")
    else:
        print(f"{block_field_player[0]} [1/1] \n")

    print(f"                                                    Discard:Player ")
    print(f"          Draw:Player                               {len(discard_pile_player)} ")

    if not draw_field_player:  # used to figure out the state of the card in play
        print(f"          [] \n")
    elif len(draw_field_player) == 3:
        print(f"          [1/2] \n")
    elif len(draw_field_player) == 2:
        print(f"          {draw_field_player[0]} [2/2] \n")
    else:
        print(f"          {draw_field_player[0]} [1/1] \n")

    print(f"                                                    Deck:Player ")
    print(f"Hand:Player                                         {len(deck_player)} ")
    if hand_player:
        print(f"{(', '.join(hand_player))} \n")
    else:
        print(f"{len(hand_player)} \n")


# start game -----------------------------------------------------------------------------------------------------------

def start_player():  # deals cards to player at the beginning
    global deck_player, hand_player

    card_player = random.choice(deck_player)  # picks random card from deck
    hand_player.append(card_player)  # puts card into the hand of the player
    deck_player.remove(card_player)  # removes card from deck


def start_bot():  # deals cards to bot at the beginning
    global deck_bot, hand_bot

    card_bot = random.choice(deck_bot)
    hand_bot.append(card_bot)
    deck_bot.remove(card_bot)


# playing cards // adding markers --------------------------------------------------------------------------------------

def play_card_player(instance):  # leads player through game interaction to put cards on fields and charge them
    global hand_player, go_back
    global attack_field_player, block_field_player, draw_field_player

    while True:
        go_back = False
        if instance is attack_field_player:
            card_player = input(f"Play:Attack ").upper()  # allows for play: n, a, p, f
        elif instance is block_field_player:
            card_player = input(f"Play:Block ").upper()
        else:
            card_player = input(f"Play:Draw ").upper()
        if card_player == "0":  # choosing to not play a card - breaking loop to advance the game
            break
        elif card_player not in hand_player:
            print("Choose Valid:Input ")  # wrong input - keeping the loop
        elif card_player in hand_player:
            instance.append(card_player)  # card is put on instance/field
            hand_player.remove(card_player)  # card is removed from hand
            while True:
                state_card_player = input("D:Direct or C:Charged? ").lower()
                if state_card_player == "d":
                    break
                elif state_card_player == "b":
                    hand_player.append(card_player)
                    instance.remove(card_player)
                    go_back = True
                    break
                elif state_card_player == "c":
                    add_marker(instance)  # putting 2 markers into the list to manipulate the length of the list
                    add_marker(instance)
                    break
                elif state_card_player != "d" or "c":
                    print("Choose Valid:Input ")
            break


def play_card_bot(instance):  # leads bot through game to put cards on fields and charge them // not used in "vs. bot"
    global hand_bot
    global attack_field_bot, block_field_bot, draw_field_bot

    while True:
        if instance is attack_field_bot:
            card_bot = input(f"bot:Attack ").upper()
        elif instance is block_field_bot:
            card_bot = input(f"bot:Block ").upper()
        else:
            card_bot = input(f"bot:Draw ").upper()
        if card_bot == "0":
            break
        elif card_bot not in hand_bot:
            print("Choose Valid:Input ")
        elif card_bot in hand_bot:
            instance.append(card_bot)
            hand_bot.remove(card_bot)
            while True:
                state_card_bot = input("D:Direct or C:Charged? ").lower()
                if state_card_bot == "d":
                    break
                elif state_card_bot == "c":
                    add_marker(instance)
                    add_marker(instance)
                    break
                elif state_card_bot != "d" or "c":
                    print("Choose Valid:Input ")
            break


def add_marker(instance):  # charging a card on a field if played manually
    global marker_bag

    marker = random.choice(marker_bag)  # taking marker from marker_bag
    instance.append(marker)  # adding it to the field
    marker_bag.remove(marker)  # removing it from marker_bag


# calculation ----------------------------------------------------------------------------------------------------------

def calc():  # large body of preparation and execution of damage and health calculation
    global game, health_player, health_bot, pre_calc_health_player, pre_calc_health_bot

    global attack_field_bot, block_field_bot, draw_field_bot
    global attack_field_player, block_field_player, draw_field_player

    global heal_player, reflect_player, block_draw_player, steal_draw_player
    global attack_player, block_player, calc_draw_player

    global heal_bot, reflect_bot, block_draw_bot, steal_draw_bot
    global attack_bot, block_bot, calc_draw_bot

    global N_attack_direct, N_block_direct, N_draw_direct, N_attack_charged, N_block_charged, N_draw_charged
    global A_attack_direct, A_block_direct, A_draw_direct, A_attack_charged, A_block_charged, A_draw_charged
    global P_attack_direct, P_block_direct, P_draw_direct, P_attack_charged, P_block_charged, P_draw_charged
    global F_attack_direct, F_block_direct, F_draw_direct, F_attack_charged, F_block_charged, F_draw_charged

    # player ----------------------------------------------------------------------------------------------

    # player attack ----------------------------------------------------------------------
    if len(attack_field_player) == 3:  # if card is freshly charged (has card and two markers in it)
        pass

    elif len(attack_field_player) == 2:  # if card is charged and ready (card and one marker in it)
        if "N" in attack_field_player:
            attack_player += N_attack_charged
        elif "A" in attack_field_player:
            attack_player += A_attack_charged
        elif "P" in attack_field_player:
            attack_player += P_attack_charged
        elif "F" in attack_field_player:
            attack_player += F_attack_charged
            heal_player = True

    elif len(attack_field_player) == 1:  # if card is played direct (no extra markers)
        if "N" in attack_field_player:
            attack_player += N_attack_direct
        elif "A" in attack_field_player:
            attack_player += A_attack_direct
        elif "P" in attack_field_player:
            attack_player += P_attack_direct
        elif "F" in attack_field_player:
            attack_player += F_attack_direct

    # player block -----------------------------------------------------------------------
    if len(block_field_player) == 3:  # if card is freshly charged
        pass

    elif len(block_field_player) == 2:  # if card is charged and ready
        if "N" in block_field_player:
            block_player += N_block_charged
        elif "A" in block_field_player:
            block_player += A_block_charged
        elif "P" in block_field_player:
            block_player += P_block_charged
        elif "F" in block_field_player:  # if 'F' is countered by 'N'
            if "N" in attack_field_bot and len(attack_field_bot) <= 2:
                pass  # not activating reflect because N is in active opposition
            else:
                reflect_player = True

    elif len(block_field_player) == 1:  # if card is played direct
        if "N" in block_field_player:
            block_player += N_block_direct
        elif "A" in block_field_player:
            block_player += A_block_direct
        elif "P" in block_field_player:
            block_player += P_block_direct
        elif "F" in block_field_player:
            block_player += F_block_direct

    # player draw ------------------------------------------------------------------------
    if len(draw_field_player) == 3:  # if card is freshly charged
        pass

    elif len(draw_field_player) == 2:  # if card is charged and ready
        if "N" in draw_field_player:
            calc_draw_player += N_draw_charged
        elif "A" in draw_field_player:
            calc_draw_player += A_draw_charged
        elif "P" in draw_field_player:
            calc_draw_player += P_draw_charged
        elif "F" in draw_field_player:  # if 'F' is countered by 'N'
            if "N" in draw_field_bot and len(draw_field_bot) <= 2:
                calc_draw_bot += 1
            elif not draw_field_bot:
                pass
            else:
                steal_draw_player = True

    elif len(draw_field_player) == 1:  # if card is played direct
        if "N" in draw_field_player:
            calc_draw_player += N_draw_direct
        elif "A" in draw_field_player:
            calc_draw_player += A_draw_direct
        elif "P" in draw_field_player:
            calc_draw_player += P_draw_direct
        elif "F" in draw_field_player:  # if 'F' is countered by 'N'
            if "N" in draw_field_bot and len(draw_field_bot) <= 2:
                calc_draw_bot += 1
            elif not draw_field_bot:
                pass
            else:
                block_draw_player = True

    # bot --------------------------------------------------------------------------------------------------

    # bot attack --------------------------------------------------------------------------
    if len(attack_field_bot) == 3:  # if card is freshly charged
        pass

    elif len(attack_field_bot) == 2:  # if card is charged and ready
        if "N" in attack_field_bot:
            attack_bot += N_attack_charged
        elif "A" in attack_field_bot:
            attack_bot += A_attack_charged
        elif "P" in attack_field_bot:
            attack_bot += P_attack_charged
        elif "F" in attack_field_bot:
            attack_bot += F_attack_charged
            heal_bot = True

    elif len(attack_field_bot) == 1:  # if card is played direct
        if "N" in attack_field_bot:
            attack_bot += N_attack_direct
        elif "A" in attack_field_bot:
            attack_bot += A_attack_direct
        elif "P" in attack_field_bot:
            attack_bot += P_attack_direct
        elif "F" in attack_field_bot:
            attack_bot += F_attack_direct

    # bot block ---------------------------------------------------------------------------
    if len(block_field_bot) == 3:  # if card is freshly charged
        pass

    elif len(block_field_bot) == 2:  # if card is charged and ready
        if "N" in block_field_bot:
            block_bot += N_block_charged
        elif "A" in block_field_bot:
            block_bot += A_block_charged
        elif "P" in block_field_bot:
            block_bot += P_block_charged
        elif "F" in block_field_bot:  # if 'F' is countered by 'N'
            if "N" in attack_field_player and len(attack_field_player) <= 2:
                pass
            else:
                reflect_bot = True

    elif len(block_field_bot) == 1:  # if card is played direct
        if "N" in block_field_bot:
            block_bot += N_block_direct
        elif "A" in block_field_bot:
            block_bot += A_block_direct
        elif "P" in block_field_bot:
            block_bot += P_block_direct
        elif "F" in block_field_bot:
            block_bot += F_block_direct

    # bot draw ----------------------------------------------------------------------------
    if len(draw_field_bot) == 3:  # if card is freshly charged
        pass

    elif len(draw_field_bot) == 2:  # if card is charged and ready
        if "N" in draw_field_bot:
            calc_draw_bot += N_draw_charged
        elif "A" in draw_field_bot:
            calc_draw_bot += A_draw_charged
        elif "P" in draw_field_bot:
            calc_draw_bot += P_draw_charged
        elif "F" in draw_field_bot:  # if 'F' is countered by 'N'
            if "N" in draw_field_player and len(draw_field_player) <= 2:
                calc_draw_player += 1
            elif not draw_field_player:
                pass
            else:
                steal_draw_bot = True

    elif len(draw_field_bot) == 1:  # if card is played direct
        if "N" in draw_field_bot:
            calc_draw_bot += N_draw_direct
        elif "A" in draw_field_bot:
            calc_draw_bot += A_draw_direct
        elif "P" in draw_field_bot:
            calc_draw_bot += P_draw_direct
        elif "F" in draw_field_bot:  # if 'F' is countered by 'N'
            if "N" in draw_field_player and len(draw_field_player) <= 2:
                calc_draw_player += 1
            elif not draw_field_player:
                pass
            else:
                block_draw_bot = True

    # formulas --------------------------------------------------------------------------------------------

    pre_calc_health_bot = health_bot  # separating old life to print it in the calculation phase
    pre_calc_health_player = health_player

    # attack bot // block player ----------------------------------------------------------
    if heal_bot is True and reflect_player is True:  # case when 'F' is charged vs. charged 'F'
        health_bot -= attack_bot
        health_player += attack_bot
    elif heal_bot is True and reflect_player is False:  # 'F' charges vs. not-"F"-block
        health_player -= (attack_bot - block_player)
        health_bot += (attack_bot - block_player)
    elif heal_bot is False and reflect_player is True:  # any non-'F'-charged-attack vs. charged 'F'
        health_bot -= attack_bot
        attack_bot = 0  # setting initial attack to zero because it's reflected
    elif heal_bot is False and reflect_player is False:  # any non-'F'-charged-attack vs. not-'F'-charged-block
        health_player -= max(0, attack_bot - block_player)  # max zero so a strong block doesn't add life

    # attack player // block bot ----------------------------------------------------------
    if heal_player is True and reflect_bot is True:
        health_player -= attack_player
        health_bot += attack_player
    elif heal_player is True and reflect_bot is False:
        health_player += attack_player - block_bot
        health_bot -= attack_player - block_bot
    elif heal_player is False and reflect_bot is True:
        health_player -= attack_player
        attack_player = 0  # setting attack to 0 because it's reflected
    elif heal_player is False and reflect_bot is False:
        health_bot -= max(0, attack_player - block_bot)  # max zero so a strong block doesn't add life

    # draw -------------------------------------------------------------------------------
    if block_draw_player is True:  # only set to true if no 'N' in active opposition
        calc_draw_bot = 0  # set to zero because it's blocked
    elif steal_draw_player is True:  # only set to true if no 'N' in active opposition
        calc_draw_player += calc_draw_bot  # stealing the draw
        calc_draw_bot = 0  # setting initial draw to zero

    if block_draw_bot is True:
        calc_draw_player = 0
    elif steal_draw_bot is True:
        calc_draw_bot += calc_draw_player
        calc_draw_player = 0

    input("\nPress Calculation:Phase ")  # printing calculation phase as overview after showdown
    print(f"")
    print(f"Bot:Attack      {attack_bot}          Heal:Bot        {heal_bot} ")
    print(f"Player:Block    {block_player}          Reflect:Player  {reflect_player} ")
    print(f"")
    print(f"Player:Attack   {attack_player}          Heal:Player     {heal_player} ")
    print(f"Bot:Block       {block_bot}          Reflect:Bot     {reflect_bot} ")
    print(f"")
    if pre_calc_health_bot < 10 and health_bot in [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]:
        print(f"Life:Bot         {pre_calc_health_bot}   -->    {health_bot} ")
    elif pre_calc_health_bot < 10 and (9 < health_bot or health_bot < 0):
        print(f"Life:Bot         {pre_calc_health_bot}   -->   {health_bot} ")
    elif pre_calc_health_bot > 9 and health_bot in [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]:
        print(f"Life:Bot        {pre_calc_health_bot}   -->    {health_bot} ")
    elif pre_calc_health_bot > 9 and (health_bot > 9 or health_bot < 0):
        print(f"Life:Bot        {pre_calc_health_bot}   -->   {health_bot} ")

    if pre_calc_health_player < 10 and health_player in [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]:
        print(f"Life:Player      {pre_calc_health_player}   -->    {health_player} ")
    elif pre_calc_health_player < 10 and (9 < health_player or health_player < 0):
        print(f"Life:Player      {pre_calc_health_player}   -->   {health_player} ")
    elif pre_calc_health_player > 9 and health_player in [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]:
        print(f"Life:Player     {pre_calc_health_player}   -->    {health_player} ")
    elif pre_calc_health_player > 9 and (health_player > 9 or health_player < 0):
        print(f"Life:Player     {pre_calc_health_player}   -->   {health_player} ")


# end_of_game ----------------------------------------------------------------------------------------------------------

def end_of_game():
    global game, health_player, health_bot
    
    if health_bot <= 0 and health_player <= 0:  # both die
        input()
        state_of_game(game)  # showing full state of game  - revealing all played cards, hands and discard piles
        print("Match:Draw ")
        game = False  # ending the game loop
    elif health_player <= 0 < health_bot:  # player dies, bot survives
        input()
        state_of_game(game)
        print("Bot:Win ")
        game = False
    elif health_bot <= 0 < health_player:  # bot dies, player survives
        input()
        state_of_game(game)
        print("Player:Win ")
        game = False


# clean-up -------------------------------------------------------------------------------------------------------------

def clean_up():  # to remove markers, activate charged cards and clean already activated cards from the board
    global marker_bag

    # player clean-up --------------------------------------------------------------------
    global attack_field_player, block_field_player, draw_field_player
    global discard_pile_player

    if not attack_field_player:
        pass
    elif len(attack_field_player) == 1:  # was a directly played card
        card_attack_player = attack_field_player[0]  # calling the card
        discard_pile_player.append(card_attack_player)  # putting it into discard
        attack_field_player = []  # cleaning field
    elif len(attack_field_player) == 2:  # a charged activated card
        card_attack_player = attack_field_player[0]  # calling first element which is always a card, not a marker
        discard_pile_player.append(card_attack_player)  # card removed from list
        marker_bag.append(1)  # last marker moves bag into marker_bag, so they can be used for next round
        attack_field_player = []  # cleaning field completely
    elif len(attack_field_player) == 3:  # a passive charged card
        attack_field_player.remove(1)  # removing one marker to properly count the charge for next round
        marker_bag.append(1)  # refilling marker_bag

    if not block_field_player:
        pass
    elif len(block_field_player) == 1:
        card_block_player = block_field_player[0]
        discard_pile_player.append(card_block_player)
        block_field_player = []
    elif len(block_field_player) == 2:
        card_block_player = block_field_player[0]
        discard_pile_player.append(card_block_player)
        marker_bag.append(1)
        block_field_player = []
    elif len(block_field_player) == 3:
        block_field_player.remove(1)
        marker_bag.append(1)

    if not draw_field_player:
        pass
    elif len(draw_field_player) == 1:
        card_draw_player = draw_field_player[0]
        discard_pile_player.append(card_draw_player)
        draw_field_player = []
    elif len(draw_field_player) == 2:
        card_draw_player = draw_field_player[0]
        discard_pile_player.append(card_draw_player)
        marker_bag.append(1)
        draw_field_player = []
    elif len(draw_field_player) == 3:
        draw_field_player.remove(1)
        marker_bag.append(1)

    # bot clean-up ------------------------------------------------------------------------
    global attack_field_bot, block_field_bot, draw_field_bot
    global discard_pile_bot

    if not attack_field_bot:
        pass
    elif len(attack_field_bot) == 1:
        card_attack_bot = attack_field_bot[0]
        discard_pile_bot.append(card_attack_bot)
        attack_field_bot = []
    elif len(attack_field_bot) == 2:
        card_attack_bot = attack_field_bot[0]
        discard_pile_bot.append(card_attack_bot)
        marker_bag.append(1)
        attack_field_bot = []
    elif len(attack_field_bot) == 3:
        attack_field_bot.remove(1)
        marker_bag.append(1)

    if not block_field_bot:
        pass
    elif len(block_field_bot) == 1:
        card_block_bot = block_field_bot[0]
        discard_pile_bot.append(card_block_bot)
        block_field_bot = []
    elif len(block_field_bot) == 2:
        card_block_bot = block_field_bot[0]
        discard_pile_bot.append(card_block_bot)
        marker_bag.append(1)
        block_field_bot = []
    elif len(block_field_bot) == 3:
        block_field_bot.remove(1)
        marker_bag.append(1)

    if not draw_field_bot:
        pass
    elif len(draw_field_bot) == 1:
        card_draw_bot = draw_field_bot[0]
        discard_pile_bot.append(card_draw_bot)
        draw_field_bot = []
    elif len(draw_field_bot) == 2:
        card_draw_bot = draw_field_bot[0]
        discard_pile_bot.append(card_draw_bot)
        marker_bag.append(1)
        draw_field_bot = []
    elif len(draw_field_bot) == 3:
        draw_field_bot.remove(1)
        marker_bag.append(1)


# reset ----------------------------------------------------------------------------------------------------------------

def reset():  # set states to default, so calculations of this round does not interfere with calculations of next round
    global attack_field_player, block_field_player, draw_field_player
    global heal_player, reflect_player, block_draw_player, steal_draw_player
    global attack_player, block_player, calc_draw_player, zcr_player

    global attack_field_bot, block_field_bot, draw_field_bot
    global heal_bot, reflect_bot, block_draw_bot, steal_draw_bot
    global attack_bot, block_bot, calc_draw_bot, zcr_bot

    heal_player = False
    reflect_player = False
    block_draw_player = False
    steal_draw_player = False
    attack_player = 0
    block_player = 0
    calc_draw_player = 0
    zcr_player = 0

    heal_bot = False
    reflect_bot = False
    block_draw_bot = False
    steal_draw_bot = False
    attack_bot = 0
    block_bot = 0
    calc_draw_bot = 0
    zcr_bot = 0


# shuffling ------------------------------------------------------------------------------------------------------------

def shuffle_p():  # shuffles discard pile into deck if deck is empty and player draws a card
    global discard_pile_player, shuffle_count_player, deck_player

    for x in range(len(discard_pile_player)):  # looped so all cards are put into deck again
        shuffle_count_player += 1  # important so "Shuffle Deck:Player" can be printed
        new_card = random.choice(discard_pile_player)  # cards from this round are in discard pile as well
        deck_player.append(new_card)  # deck will be filled with new cards
        discard_pile_player.remove(new_card)  # discard pile is being emptied again


def shuffle_c():
    global discard_pile_bot, shuffle_count_bot, deck_bot

    for x in range(len(discard_pile_bot)):
        shuffle_count_bot += 1
        new_card = random.choice(discard_pile_bot)
        deck_bot.append(new_card)
        discard_pile_bot.remove(new_card)


# drawing --------------------------------------------------------------------------------------------------------------

# draw player ------------------------------------------------------------------------
def draw_p():  # draw function for player - only draws up to one card
    global card_draw_count_player
    global deck_player, hand_player

    if deck_player:  # important so program only draws from existing deck
        card_draw_count_player += 1  # will be displayed in "draw:phase"
        card_player = deck_player[0]  # always drawing first card
        hand_player.append(card_player)  # card is put in hand
        deck_player.remove(card_player)  # card is removed from deck
    else:  # activates if deck is empty
        shuffle_p()  # shuffles discard pile into deck
        if deck_player:  # drawing again if anything got shuffled
            card_draw_count_player += 1
            card_player = deck_player[0]
            hand_player.append(card_player)
            deck_player.remove(card_player)


# draw bot ----------------------------------------------------------------------------
def draw_c():
    global card_draw_count_bot
    global deck_bot, hand_bot

    if deck_bot:
        card_draw_count_bot += 1
        card_bot = deck_bot[0]
        hand_bot.append(card_bot)
        deck_bot.remove(card_bot)
    else:
        shuffle_c()
        if not deck_bot:
            pass
        else:
            card_draw_count_bot += 1
            card_bot = deck_bot[0]
            hand_bot.append(card_bot)
            deck_bot.remove(card_bot)


# actual drawing --------------------------------------------------------------------------------------
def actual_drawing():  # final draw calculation, loop for drawing and print "draw:phase"
    global health_player, hand_player, draw_player, calc_draw_player, zcr_player
    global health_bot, hand_bot, draw_bot, calc_draw_bot, zcr_bot
    global card_draw_count_bot, card_draw_count_player

    if not hand_player and health_player < 4:
        zcr_player += 2  # zero card rule if low life and no hand
    elif not hand_player and health_player > 3:
        zcr_player += 1  # zero card rule if no hand
    draw_player = calc_draw_player + zcr_player  # adding draws from cards in play and zero card rule
    if draw_player > 0:
        for dp in range(draw_player):  # loops the draw_p() which only draws up to one card
            draw_p()

    if not hand_bot and health_bot < 4:
        zcr_bot += 2
    elif not hand_bot and health_bot > 3:
        zcr_bot += 1
    draw_bot = calc_draw_bot + zcr_bot
    if draw_bot > 0:
        for dc in range(draw_bot):
            draw_c()

    input("\n\nPress Draw:Phase ")  # shows player how many cards were actually drawn
    print(f"\nbot:Draw       {card_draw_count_bot} ")
    print(f"Player:Draw   {card_draw_count_player} \n")

    if shuffle_count_bot != 0:  # informs player that decks have been shuffled
        print(f"Shuffle Deck:bot ")
    if shuffle_count_player != 0:
        print(f"Shuffle Deck:Player \n")


# instances ------------------------------------------------------------------------------------------------------------

def attack():  # gives options to attack for player/bot
    global hand_player, attack_field_player, go_back
    global hand_bot, attack_field_bot

    print("\nInstance:Attack ")
    print(" ")
    if attack_field_player:  # a card has already been played
        input("Player:charged ")
    elif not hand_player:  # hand empty
        input("Player Hand:Empty ")
    elif not attack_field_player:  # field empty and card(s) in hand - option to play something
        play_card_player(attack_field_player)
        while True:
            if go_back is True:
                play_card_player(attack_field_player)
            else:
                break
    if attack_field_bot:
        print("bot:charged ")
    elif not hand_bot:
        print("bot Hand:Empty ")
    elif not attack_field_bot:
        play_bot(attack_field_bot)
    turn()  # printing the game board without revealing enemy cards


def block():  # gives options to block for player/bot
    global hand_player, block_field_player, go_back
    global hand_bot, block_field_bot, reserve_block

    print("\nInstance:Block ")
    print(" ")
    if block_field_player:
        input("Player:charged ")
    elif not hand_player:
        input("Player Hand:Empty ")
    elif not block_field_player:
        play_card_player(block_field_player)
        while True:
            if go_back is True:
                play_card_player(block_field_player)
            else:
                break
    if block_field_bot:
        print("bot:charged ")
    elif not hand_bot and not reserve_block:
        print("bot Hand:Empty ")
    elif not block_field_bot:
        play_bot(block_field_bot)
    turn()


def draw():  # gives options to draw for player/bot
    global hand_player, draw_field_player, go_back
    global hand_bot, draw_field_bot, reserve_draw

    print("\nInstance:Draw ")
    print(" ")
    if draw_field_player:
        input("Player:charged ")
    elif not hand_player:
        input("Player Hand:Empty ")
    elif not draw_field_player:
        play_card_player(draw_field_player)
        while True:
            if go_back is True:
                play_card_player(draw_field_player)
            else:
                break
    if draw_field_bot:
        print("bot:charged ")
    elif not hand_bot and not reserve_draw:
        print("bot Hand:Empty ")
    elif not draw_field_bot:
        play_bot(draw_field_bot)
    turn()


# start next round -----------------------------------------------------------------------------------------------------

def next_round():  # adds 1 to rounds, resets count variables
    global rounds
    global card_draw_count_player, shuffle_count_player
    global card_draw_count_bot, shuffle_count_bot

    card_draw_count_player = 0
    shuffle_count_player = 0

    card_draw_count_bot = 0
    shuffle_count_bot = 0

    rounds += 1
    if rounds > 1:  # if in round 1 this is not necessary, only starts at round 2
        input("\nPress Next:Round ")
    turn()


# bot protocol ---------------------------------------------------------------------------------------------------------

def pan(instance, percent):  # making strong play - leaving out 'F' - instance and percent arguments for flexibility
    global hand_bot, reserve_block, reserve_draw

    x = random.choice(percent)  # adding chance condition
    if x == 1:
        if instance is block_field_bot and reserve_block:  # takes card from reserve field first if one is there
            card_bot = reserve_block[0]
            instance.append(card_bot)
            reserve_block.remove(card_bot)
        elif instance is draw_field_bot and reserve_draw:
            card_bot = reserve_draw[0]
            instance.append(card_bot)
            reserve_draw.remove(card_bot)
        elif 'P' in hand_bot:  # first checking P to make a stronger play
            play_specific(instance, 'P', percent)  # only trying to play P
        elif 'A' in hand_bot:
            play_specific(instance, 'A', percent)
        elif 'N' in hand_bot:
            play_specific(instance, 'N', percent)


def nap(instance, percent):  # whole thing reversed to pan
    global hand_bot, reserve_block, reserve_draw

    x = random.choice(percent)
    if x == 1:
        if instance is block_field_bot and reserve_block:
            card_bot = reserve_block[0]
            instance.append(card_bot)
            reserve_block.remove(card_bot)
        elif instance is draw_field_bot and reserve_draw:
            card_bot = reserve_draw[0]
            instance.append(card_bot)
            reserve_draw.remove(card_bot)
        elif 'N' in hand_bot:
            play_specific(instance, 'N', percent)
        elif 'A' in hand_bot:
            play_specific(instance, 'A', percent)
        elif 'P' in hand_bot:
            play_specific(instance, 'P', percent)


def charge_(instance, percent):  # extra function for charging the card played by the bot
    global marker_bag

    if len(marker_bag) >= 2:  # can only take markers if some are in the marker_bag
        x = random.choice(percent)  # adding chance for unpredictability
        if x == 1:
            add_marker(instance)
            add_marker(instance)


def play_specific(instance, card, percent):  # plays specific card if available
    global hand_bot, reserve_block, reserve_draw
    global block_field_bot, draw_field_bot

    x = random.choice(percent)
    if x == 1:
        if instance is block_field_bot and reserve_block:  # conditions for playing in block
            instance.append(card)  # card is being put onto the field
            reserve_block.remove(card)
        elif instance is draw_field_bot and reserve_draw:
            instance.append(card)
            reserve_draw.remove(card)
        elif card in hand_bot:
            instance.append(card)
            hand_bot.remove(card)


def set_aside_block():  # puts card into extra list to not have the computer play it in attack
    global hand_bot, reserve_block, block_field_bot
    global attack_field_player

    if not reserve_block and not block_field_bot:
        if 'P' in hand_bot:
            set_card = 'P'
            reserve_block.append(set_card)
            hand_bot.remove(set_card)
        elif 'A' in hand_bot:
            set_card = 'A'
            reserve_block.append(set_card)
            hand_bot.remove(set_card)
        elif 'F' in hand_bot and len(attack_field_player) == 3:
            set_card = 'F'
            reserve_block.append(set_card)
            hand_bot.remove(set_card)
        elif 'N' in hand_bot:
            set_card = 'N'
            reserve_block.append(set_card)
            hand_bot.remove(set_card)


def set_aside_draw():
    global draw_field_bot, reserve_draw, health_bot, hand_bot

    if not reserve_draw and not draw_field_bot:
        set_card = random.choice(hand_bot)  # no preferences to which card
        reserve_draw.append(set_card)  # puts card in the reserve list
        hand_bot.remove(set_card)  # removes card from hand


def play_random(instance, percent):  # butter function to have the player guessing
    global hand_bot, reserve_block, reserve_draw, block_field_bot, draw_field_bot

    x = random.choice(percent)
    if x == 1:
        if instance is block_field_bot and reserve_block:
            card_bot = reserve_block[0]
            instance.append(card_bot)
            reserve_block.remove(card_bot)
        elif instance is draw_field_bot and reserve_draw:
            card_bot = reserve_draw[0]
            instance.append(card_bot)
            reserve_draw.remove(card_bot)
            if card_bot == 'N':
                charge_(instance, hundred)
        else:
            if hand_bot:
                card_bot = random.choice(hand_bot)
                instance.append(card_bot)
                hand_bot.remove(card_bot)


def activating_afs():
    global attack_frenzy_system, health_player, afs_switch

    if attack_frenzy_system is True:
        afs_switch = 1
    elif attack_frenzy_system is False:
        afs_switch = 0

    if health_player < 10:
        attack_frenzy_system = True
        if afs_switch == 0:
            print(f"\n\n------------------------------------------------")
            print(f"                 Attack:Frenzy ")
            print(f"                System:Activated ")
            input(f"------------------------------------------------\n\n")
    elif health_player > 9:
        attack_frenzy_system = False
        if afs_switch == 1:
            print(f"\n\n------------------------------------------------")
            print(f"                 Attack:Frenzy ")
            print(f"               System:Deactivated ")
            input(f"------------------------------------------------\n\n")


def play_bot(instance):  # basis for choice is set
    global discard_pile_player, deck_player, health_player
    global attack_field_player, block_field_player, draw_field_player
    global attack_field_bot, block_field_bot, draw_field_bot
    global reserve_block, reserve_block, attack_frenzy_system, hand_bot, show_hand_bot

# attack frenzy system ON -----------------------------------------------------------------------------
    if attack_frenzy_system is True:
        if instance is attack_field_bot:  # panning for maximum pressure
            if 'P' in hand_bot:  # checking whether card is actually there
                play_specific(instance, 'P', hundred)
                charge_(instance, ten)
            elif 'A' in hand_bot:
                play_specific(instance, 'A', hundred)
                charge_(instance, ten)
            elif 'N' in hand_bot:
                play_specific(instance, 'N', hundred)
                if 'F' not in discard_pile_player and 'F' not in deck_player:
                    charge_(instance, ninety)
                else:
                    charge_(instance, ten)
            elif 'F' in hand_bot:
                play_specific(instance, 'F', five)
                if 'F' in discard_pile_player or 'F' in deck_player:
                    play_specific(instance, 'F', hundred)
                    charge_(instance, hundred)

        if instance is block_field_bot:
            if len(attack_field_player) == 2:
                if 'A' in hand_bot and 'P' in hand_bot:
                    play_specific(instance, 'P', seventy)
                    if not instance:
                        play_specific(instance, 'A', hundred)
                elif 'A' in hand_bot:
                    play_specific(instance, 'A', hundred)
                elif 'P' in hand_bot:
                    play_specific(instance, 'P', hundred)
                elif 'N' in hand_bot:
                    play_specific(instance, 'N', hundred)

            elif len(attack_field_player) == 1:
                if health_bot < 2:
                    play_specific(instance, 'P', hundred)
                    if not instance:
                        play_specific(instance, 'A', hundred)
                        if not instance:
                            play_specific(instance, 'N', hundred)
                elif health_bot < 4:
                    play_specific(instance, 'N', hundred)
                    if not instance:
                        play_specific(instance, 'A', hundred)
                        if not instance:
                            play_specific(instance, 'P', hundred)

            elif len(attack_field_player) == 3:
                if 'F' in hand_bot:
                    play_specific(instance, 'F', ninety)
                    if block_field_bot:
                        charge_(instance, hundred)
                if not instance and 'A' in hand_bot:
                    play_specific(instance, 'A', eighty)
                    charge_(instance, hundred)
                if not instance and 'N' in hand_bot:
                    play_specific(instance, 'N', sixty)
                    charge_(instance, hundred)
                if not instance and 'P' in hand_bot:
                    play_specific(instance, 'P', hundred)
                    charge_(instance, hundred)

            elif len(hand_bot) == 2:
                if 'P' in hand_bot:
                    if 'A' in hand_bot:
                        play_specific(instance, 'A', hundred)
                    elif 'N' in hand_bot:
                        play_specific(instance, 'N', hundred)
                    elif 'F' in hand_bot:
                        play_specific(instance, 'F', hundred)
                    else:
                        play_specific(instance, 'P', hundred)
                elif 'A' in hand_bot:
                    if 'N' in hand_bot:
                        play_specific(instance, 'N', hundred)
                    elif 'F' in hand_bot:
                        play_specific(instance, 'F', hundred)
                elif 'N' in hand_bot:
                    play_random(instance, hundred)

        if instance is draw_field_bot:
            if len(hand_bot) == 1:
                play_random(instance, hundred)
                if 'N' in draw_field_bot:
                    charge_(instance, hundred)
                elif 'F' in draw_field_bot:
                    charge_(instance, thirty)
                elif 'A' in draw_field_bot:
                    charge_(instance, eighty)
                elif 'P' in draw_field_bot:
                    charge_(instance, twenty)
            elif 'A' in hand_bot:
                play_specific(instance, 'A', hundred)
                charge_(instance, eighty)
            elif 'N' in hand_bot:
                play_specific(instance, 'N', hundred)
                charge_(instance, ninetyfive)
            elif 'F' in hand_bot:
                play_specific(instance, 'F', seventy)
                if len(draw_field_player) == 3:
                    charge_(instance, hundred)
            elif 'P' in hand_bot:
                play_specific(instance, 'P', hundred)
                charge_(instance, thirty)

# attack frenzy system OFF ----------------------------------------------------------------------------
    if attack_frenzy_system is False:
        if instance is attack_field_bot:  # attack choice system
            if health_bot < 8 and attack_field_player:  # check if low health and no card set aside
                set_aside_block()  # then reserving card to prioritize blocking over attacking
            if not draw_field_bot and len(hand_bot) in [1, 2]:
                set_aside_draw()  # reserves card for draw if no draw already, low hand cards and nothing set aside yet
            if len(block_field_player) == 2:  # counter charging to hit player as strongly as possible
                play_random(instance, hundred)
                if attack_field_bot:  # only charging if a card has been played - otherwise no card but 1's are added
                    add_marker(instance)
                    add_marker(instance)
            else:
                play_random(instance, hundred)  # choosing any card if above options are not triggered
                if 'F' in attack_field_bot and len(attack_field_bot) == 1:  # charge 'F' otherwise it's value is zero
                    if 'F' in discard_pile_player or 'F' in deck_player:
                        charge_(instance, hundred)
                    else:
                        charge_(instance, fifty)
                else:
                    if attack_field_bot:
                        if 'F' in discard_pile_player or 'F' in deck_player:
                            charge_(instance, hundred)  # no danger from being reflected
                        else:
                            charge_(instance, one_third)  # charging one third of the time

        if instance is block_field_bot:  # block choice system
            if not draw_field_bot and len(hand_bot) in [1, 2] and not reserve_draw:
                set_aside_draw()  # reserves card for draw if no draw already, low hand cards and nothing set aside yet
            if not attack_field_player:  # skipping block if player doesn't attack
                pass
            elif len(attack_field_player) == 3:  # if player comes charged
                play_random(instance, hundred)
                if block_field_bot:  # if blocked, definitely charge to maximize block
                    add_marker(instance)
                    add_marker(instance)
            elif len(attack_field_player) in [1, 2]:  # if attack activates this round block direct and not with 'F'
                pan(instance, hundred)

        if instance is draw_field_bot:  # draw choice system
            if reserve_draw:
                play_random(instance, hundred)  # picking a card from reserve if there
            else:
                pan(instance, hundred)
                charge_(instance, one_third)
