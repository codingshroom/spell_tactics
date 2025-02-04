import random  # to shuffle cards/decks

current_round = 0  # counter to keep track of where the game is - charging and other stuff build on this

class Player: # structure for players
    def __init__(self, name, card_data):  # card_data allowing for different starting decks
        self.name = name
        self.health = 13  # starting health
        self.card_dictionary = {name: self.Card(name, data) for name, data in card_data.items()}  # to refer to card objects
        self.deck = list(self.card_dictionary.values())  # filling deck with all card objects
        random.shuffle(self.deck)  # randomizing starting deck order
        self.hand = []  # empty hand
        self.fields = {"attack": [], "block": [], "draw": []}  # empty playing fields
        self.discard_pile = []  # empty discard pile

    class Card:  # structure for cards
        def __init__(self, name, data, charge=False, resolve=current_round):
            self.name = name
            self.data = data  # encapsulates specific data to card object
            self.charge = charge  # safes charge of the card, is being changed by player in play()
            self.resolve = resolve  # defines in which round the card is being resolved - changes throughout the game

        def get_value(self, mode):  # accessing data of cards
            return self.data.get(mode, {})  # option to get single value '[]' or all values for mode


BASIC_CARD_DATA = {  # separation in direct & charged allows for a flexible way to get to the values
            "N": {
                "direct": {"attack": 1, "block": 1, "draw": 0, "lifesteal": False, "reflection": False, "block_draw": False, "steal_draw": False},
                "charged": {"attack": 2, "block": 2, "draw": 1, "lifesteal": False, "reflection": False, "block_draw": False, "steal_draw": False},
            },
            "A": {
                "direct": {"attack": 2, "block": 2, "draw": 1, "lifesteal": False, "reflection": False, "block_draw": False, "steal_draw": False},
                "charged": {"attack": 4, "block": 3, "draw": 2, "lifesteal": False, "reflection": False, "block_draw": False, "steal_draw": False},
            },
            "A*": {
                "direct": {"attack": 2, "block": 2, "draw": 1, "lifesteal": False, "reflection": False, "block_draw": False, "steal_draw": False},
                "charged": {"attack": 4, "block": 3, "draw": 2, "lifesteal": False, "reflection": False, "block_draw": False, "steal_draw": False},
            },
            "P": {
                "direct": {"attack": 3, "block": 3, "draw": 2, "lifesteal": False, "reflection": False, "block_draw": False, "steal_draw": False},
                "charged": {"attack": 6, "block": 4, "draw": 3, "lifesteal": False, "reflection": False, "block_draw": False, "steal_draw": False},
            },
            "P*": {
                "direct": {"attack": 3, "block": 3, "draw": 2, "lifesteal": False, "reflection": False, "block_draw": False, "steal_draw": False},
                "charged": {"attack": 6, "block": 4, "draw": 3, "lifesteal": False, "reflection": False, "block_draw": False, "steal_draw": False},
            },
            "F": {
                "direct": {"attack": 0, "block": 0, "draw": 0, "lifesteal": False, "reflection": False, "block_draw": True, "steal_draw": False},
                "charged": {"attack": 4, "block": 0, "draw": 0, "lifesteal": True, "reflection": True, "block_draw": False, "steal_draw": True},
            }
        }

action_list = ["attack", "block", "draw"]

def move_card(from_zone, to_zone):  # changes position of cards throughout the round/game
    card = from_zone[0]  # declaring card
    to_zone.append(card)
    from_zone.remove(card)

def select_card(player, card):  # calling card object
    selected_card = player.card_dictionary.get(card)  # accessing card object through card_dictionary
    return selected_card

def charge_card(card):  # saves charge information of card object into attributes
    vars(card)["charged"] = True  # used for calculation
    vars(card)["resolve"] = current_round + 1  # used for processing fields


def reset_card(card):  # resets charge information in attributes
    vars(card)["charged"] = False  # no charge is default
    vars(card)["resolve"] = current_round  # current_round for resolve is default


def play_card(player):  # structure to pick a card for play for specific player
    for action in player.fields:  # iterating over all (3) fields
        card_name = input("play card: ")  # getting card name from input
        card = select_card(player, card_name)  # calling corresponding card object
        mode = input("pick mode: ")  # getting mode (direct/charged) from input
        if mode == "charged":  # checking for charged
            charge_card(card)  # changing attributes and saving into object information
        move_card(player.deck, player.fields[action])  #  player.deck is wrong!!! player.hand later please!!!
        # print(vars(card)["resolve"]) // little cheat code to see how to access the card object attributes


def process_fields():  # cleaning fields, resetting charge information of cards
    for player in player_list:  # for both players
        for action in player.fields:  # for all fields (attack/block/draw)
            print(player.fields[action])
            card = player.fields[action][0]
            print(card)
            resolve_info = 0
            if resolve_info <= current_round:  # checking if resolve is current_round
                print("processing")


player_1 = Player("0297", BASIC_CARD_DATA)
player_2 = Player("hell boy", BASIC_CARD_DATA)

player_list = (player_1, player_2)

while True:
    play_card(player_1)
    process_fields()



