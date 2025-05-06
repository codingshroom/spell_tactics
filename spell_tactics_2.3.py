# functions with clear input(arguments) + output(return statements)
# using strengths of Classes, manipulating fields & cards directly in Player object
# adding clear interface to send information from game mechanics to GUI

import random
from dataclasses import dataclass
from typing import List, Dict

BASIC_DECK = {  # separation in direct & charged allows for a flexible way to get to the values
    "N": {  # novice spell
        "direct": {"attack": 1, "block": 1, "draw": 0, "counter": True, "lifesteal": False, "reflection": False,
                   "block_draw": False, "steal_draw": False},
        "charged": {"attack": 2, "block": 2, "draw": 1, "counter": True, "lifesteal": False, "reflection": False,
                    "block_draw": False, "steal_draw": False},
    },
    "A": {  # academy spell
        "direct": {"attack": 2, "block": 2, "draw": 1, "counter": False, "lifesteal": False, "reflection": False,
                   "block_draw": False, "steal_draw": False},
        "charged": {"attack": 4, "block": 3, "draw": 2, "counter": False, "lifesteal": False, "reflection": False,
                    "block_draw": False, "steal_draw": False},
    },
    "A*": {  # academy spell
        "direct": {"attack": 2, "block": 2, "draw": 1, "counter": False, "lifesteal": False, "reflection": False,
                   "block_draw": False, "steal_draw": False},
        "charged": {"attack": 4, "block": 3, "draw": 2, "counter": False, "lifesteal": False, "reflection": False,
                    "block_draw": False, "steal_draw": False},
    },
    "P": {  # professors spell
        "direct": {"attack": 3, "block": 3, "draw": 2, "counter": False, "lifesteal": False, "reflection": False,
                   "block_draw": False, "steal_draw": False},
        "charged": {"attack": 6, "block": 4, "draw": 3, "counter": False, "lifesteal": False, "reflection": False,
                    "block_draw": False, "steal_draw": False},
    },
    "P*": {  # professors spell
        "direct": {"attack": 3, "block": 3, "draw": 2, "counter": False, "lifesteal": False, "reflection": False,
                   "block_draw": False, "steal_draw": False},
        "charged": {"attack": 6, "block": 4, "draw": 3, "counter": False, "lifesteal": False, "reflection": False,
                    "block_draw": False, "steal_draw": False},
    },
    "F": {  # forbidden one
        "direct": {"attack": 0, "block": 0, "draw": 0, "counter": False, "lifesteal": False, "reflection": False,
                   "block_draw": True, "steal_draw": False},
        "charged": {"attack": 4, "block": 0, "draw": 0, "counter": False, "lifesteal": True, "reflection": True,
                    "block_draw": False, "steal_draw": True},
    }
}

class Game:
    def __init__(self):
        self.round = 0

    def overview(self, moment, player_1, player_2):
        print(f"\n\n---------- round: {self.round} ---------- {moment} ----------\n")

        zones_dict_1 = {"deck": player_1.deck, "hand": player_1.hand, "attack": player_1.fields["attack"],
                        "block": player_1.fields["block"],
                        "draw": player_1.fields["draw"], "discard": player_1.discard}
        zones_dict_2 = {"deck": player_2.deck, "hand": player_2.hand, "attack": player_2.fields["attack"],
                        "block": player_2.fields["block"],
                        "draw": player_2.fields["draw"], "discard": player_2.discard}

        print(f"{player_1.name}: ")
        print(f"health:".ljust(11, " "), player_1.health)
        for zone in zones_dict_1:
            print(f"{zone}:".ljust(12, " "), end=""), self.print_cards(zones_dict_1.get(zone))

        print(f"\n{player_2.name}: ")
        print(f"health:".ljust(11, " "), player_2.health)
        for zone in zones_dict_2:
            print(f"{zone}:".ljust(12, " "), end=""), self.print_cards(zones_dict_2.get(zone))

    @staticmethod
    def print_cards(zone):  # help function for printing cards in zones
        if zone:  # checking if cards in zone
            card_info = [f"{card.name} {card.charge, card.resolve}" for card in zone if
                         card is not None]  # compiling list with card name, charge, resolve information
            return print(", ".join(card_info))
        print("")

class Card:
    def __init__(self, name, data, charge="direct", resolve=0):
        self.name = name
        self.data = data  # holds values and special effects for calculation
        self.charge = charge  # basis for calculation
        self.resolve = resolve  # when to calculate

    def get_value(self, mode):
        return self.data.get(mode, {})  # accessing specific value

    def update_mode(self, mode, game_round):
        if mode == "D":
            self.charge = "direct"
            self.resolve = game_round
        if mode == "C":
            self.charge = "charged"
            self.resolve = game_round + 1

class Player:
    def __init__(self, name, deck, health):
        self.name = name
        self.health = health
        self.card_dict = {name: Card(name, data) for name, data in deck.items()}  # mapping card.name to card objects
        self.deck = list(self.card_dict.values())  # adding each created card object to deck
        random.shuffle(self.deck)  # randomizing order
        self.hand = []
        self.fields = {"attack": [], "block": [], "draw": []}  # allows for iterating over all three fields
        self.discard = []

    def initial_deal(self, amount):  # dealing four cards
        for i in range(amount):
            if self.deck:
                card = self.deck[0]
                self.deck.remove(card)
                self.hand.append(card)

    def select_card(self, action):  # player picks a card from their hand
        if self.hand:  # checking if cards in hand
            while True:  # looping until: card from hand or skip ("0")
                card_name = input(f"\n{self.name} pick a card for {action}: ").upper()
                if card_name == "0":
                    return None
                card = self.card_dict.get(card_name)  # getting card object
                if card in self.hand:  # checking validity of play
                    return card
                print("choose a valid option")
        print("\nyour hand is empty")
        return None

    @staticmethod
    def select_mode(card):  # player selects a mode for the card they are playing
        if card is not None:
            while True:  # looping until: "C" or "D"
                mode = input("[D] for direct, [C] for charged: ").upper()
                if mode in ["C", "D"]:
                    return mode  # returning "C" for charged or "D" for direct
                print("choose a valid option")#

    def new_hand(self, card):
        if card is not None:
            self.hand.remove(card)

    def new_field(self, action, card):
        if card is not None:
            self.fields[action].append(card)

    def play_card(self, action, game_round):  # putting a card from players hand to the field with/-out charge
        if self.fields[action]:  # not allowing play if the field has a card already
            input(f"\nyou already have a card in {action}")
        else:
            card = self.select_card(action)  # picking card
            mode = self.select_mode(card)  # picking mode: charged or direct
            if card:
                card.update_mode(mode, game_round)  # changing attributes of selected card
            self.new_hand(card)  # updating hand
            self.new_field(action, card)  # updating field

    def draw_cards(self, card_amount):
        overdraw_counter = 0  # saves the amount of cards that cannot be drawn due to an empty deck
        if card_amount != 0:
            draw_flat = min(len(self.deck), card_amount)  # amount of cards that player can draw from his current deck
            draw_shuffle = max(card_amount - len(self.deck), 0)  # amount of cards that player will draw from his deck after it has been shuffled
            overdraw_counter += self.actual_draw(draw_flat, overdraw_counter)
            if draw_shuffle > 0:
                self.shuffle()
                overdraw_counter += self.actual_draw(draw_shuffle, overdraw_counter)
        return overdraw_counter

    def actual_draw(self, amount, overdraw_counter):
        for i in range(amount):
            if self.deck:
                card = self.deck[0]
                self.deck.remove(card)
                self.hand.append(card)
            else:
                overdraw_counter += 1
        return overdraw_counter

    def shuffle(self):
        for i in range(len(self.discard)):
            card = self.discard[0]
            self.deck.append(card)
            self.discard.remove(card)
        random.shuffle(self.deck)

    def clean_up(self, game_round):
        for action in self.fields:
            if self.fields[action]:
                card = self.fields[action][0]
                if card.resolve == game_round:
                    card.update_mode("D", game_round)
                    self.fields[action].remove(card)
                    self.discard.append(card)

    def zero_card_rule(self):  # players should draw a card if their hand is empty, and 2 if they have 3 or less health
        if self.hand:
            zcr_bonus = 0
        else:  # hand is empty
            if self.health <= 3:
                zcr_bonus = 2
            else:
                zcr_bonus = 1
        return zcr_bonus

@dataclass
class Zone:
    cards: List[Card]
    visible: bool
    fallback: str

class Interface:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1_dict: Dict[str, Zone] = {  # structure: [zone, show?, fallback]
            "deck": Zone(p1.deck, False, "length"),
            "hand": Zone(p1.hand, True, "length"),
            "attack": Zone(p1.fields["attack"], True, "charge_and_reveal"),
            "block": Zone(p1.fields["block"], True, "charge_and_reveal"),
            "draw": Zone(p1.fields["draw"], True, "charge_and_reveal"),
            "discard": Zone(p1.discard, True, "length")
        }
        self.p2_dict: Dict[str, Zone] = {  # structure: [zone, show_it?, what_to_show_if_not_show]
            "deck": Zone(p2.deck, False, "length"),
            "hand": Zone(p2.hand, True, "length"),
            "attack": Zone(p2.fields["attack"], True, "charge_and_reveal"),
            "block": Zone(p2.fields["block"], True, "charge_and_reveal"),
            "draw": Zone(p2.fields["draw"], True, "charge_and_reveal"),
            "discard": Zone(p2.discard, True, "length")
        }
        self.dict_list = [self.p1_dict, self.p2_dict]

    def update_dict(self, moment, perspective, game_round):  # checking for perspective and changing boolean to whether zone will be shown or not
        if perspective in ["god", "viewer"]:
            for dictionary in self.dict_list:
                for key in dictionary:
                    zone = dictionary[key]
                    zone.visible = True  # "god" sees everything
                    if perspective == "viewer" and key == "deck":  # viewer sees everything but decks of players
                        zone.visible = False
        elif perspective in ["p1", "p2"]:
            self.moment_based_update(moment, perspective, game_round)

    def moment_based_update(self, moment, perspective, game_round):
        for dictionary in self.dict_list:
            dictionary["deck"].visible = False  # both decks are never visible for players
            dictionary["discard"].visible = True  # both discards are always visible for players
        for key in list(self.p1_dict)[1:5]:  # hand, attack, block, draw --> always visible to self, not visible for opponent (unless: "reveal"/"calculation")
            self.p1_dict[key].visible = True
            self.p2_dict[key].visible = False
        if perspective == "p2":
            self.p1_dict, self.p2_dict = self.p2_dict, self.p1_dict
        if moment in ["reveal", "calculation"]:
            self.get_specifics(game_round)

    def get_specifics(self, game_round):
        for dictionary in self.dict_list:
            for key in list(dictionary)[2:5]:  # attack, block, draw  --> visible if card.resolve
                zone = dictionary[key]
                if zone.cards:
                    card = zone.cards[0]
                    if card.resolve == game_round:
                        zone.visible = True

class Print:
    def __init__(self, p1, p2, dict_1, dict_2):
        self.health_1 = p1.health
        self.deck_1 = self.read_out(dict_1, "deck")
        self.hand_1 = self.read_out(dict_1, "hand")
        self.attack_1 = self.read_out(dict_1, "attack")
        self.block_1 = self.read_out(dict_1, "block")
        self.draw_1 = self.read_out(dict_1, "draw")
        self.discard_1 = self.read_out(dict_1, "discard")

        self.health_2 = p2.health
        self.deck_2 = self.read_out(dict_2, "deck")
        self.hand_2 = self.read_out(dict_2, "hand")
        self.attack_2 = self.read_out(dict_2, "attack")
        self.block_2 = self.read_out(dict_2, "block")
        self.draw_2 = self.read_out(dict_2, "draw")
        self.discard_2 = self.read_out(dict_2, "discard")

    @staticmethod
    def read_out(dictionary, key):
        zone = dictionary[key]
        if zone.visible:  # checks boolean whether to show cards in zone
            return zone.cards if zone.cards else []  # zone as list or empty list
        if zone.fallback == "length":  # prior boolean check is wrong therefore checking what to show
            return len(zone.cards)  # showing length of zone
        if zone.cards:  # checks if zone has cards
            card = zone.cards[0]
            charge = card.charge
            resolve = card.resolve
            return str(charge) + str(resolve)
        return []  # will be activated if there is no card in fields, in that case we want to print an empty list

    @staticmethod
    def alignment(total_line, fill, *content_index_pairs):  # cleanly separates space in one line
        line = list(fill * total_line)
        for i in range(0, len(content_index_pairs), 2):  # loops through once for every content_index_pair
            if type(content_index_pairs[i]) is list:
                str_list = [card.name for card in content_index_pairs[i]]
                content = "[" + ", ".join(str_list) + "]"
            else:
                content = str(content_index_pairs[i])
            index = content_index_pairs[i + 1] or total_line // 2  # Default to center if None // what None?
            start = index - len(content) // 2
            line[start:start + len(content)] = content  # replacing line with content
        return "".join(line)

    def print_game_board(self, game_round, moment, total_line=0):
        total_line = 100 if total_line < 100 else total_line
        line_1 = int(0.12 * total_line)
        line_2 = total_line // 3 + int(0.06 * total_line)
        line_3 = total_line - line_2
        line_4 = total_line - line_1

        print()
        print(self.alignment(total_line // 2, "<>", f" round: {game_round} ", total_line // 3, f" {moment} ", total_line // 3 * 2)), print()
        print(self.alignment(total_line, " ", "hand", None))
        print(self.alignment(total_line, " ", self.hand_2, None)), print()
        print(self.alignment(total_line, " ", "deck", line_1, "draw", None))
        print(self.alignment(total_line, " ", self.deck_2, line_1, self.draw_2, None)), print()
        print(self.alignment(total_line, " ", "discard", line_1, "block", line_2, "attack", line_3, "health", line_4))
        print(self.alignment(total_line, " ", self.discard_2, line_1, self.block_2, line_2, self.attack_2, line_3, self.health_2, line_4)), print("\n")
        print(self.alignment(total_line, "-", )), print("\n")
        print(self.alignment(total_line, " ", "discard", line_1, "attack", line_2, "block", line_3, "health", line_4))
        print(self.alignment(total_line, " ", self.discard_1, line_1, self.attack_1, line_2, self.block_1, line_3, self.health_1, line_4)), print()
        print(self.alignment(total_line, " ", "deck", line_1, "draw", None))
        print(self.alignment(total_line, " ", self.deck_1, line_1, self.draw_1, None)), print()
        print(self.alignment(total_line, " ", "hand", None))
        print(self.alignment(total_line, " ", self.hand_1, None)), print()
        print(self.alignment(total_line // 2, "<>"))
        print()

def separate_card(field):  # getting card object from field
    if field:
        card = field[0]
        return card
    return None

def set_calc_value(card, action, game_round):
    value = 0
    if card:
        if card.resolve == game_round:  # checking if card should be resolved this round
            if card.charge == "charged":  # card has been charged
                value = card.get_value("charged")[action]  # accessing charged value of card in field
            else:  # card is direct
                value = card.get_value("direct")[action]  # accessing direct value of card in field
    return value

def calc_dmg(attack_value, block_value):
    damage = max(0, attack_value - block_value)  # calculating damage, not allowing negative
    return damage

def warp_dmg(damage, attack_card, block_card):
    damage_1, damage_2 = 0, 0  # damage_1 is the damage the attacker inflicts, damage_2 is the damage the attacker receives
    reflection = False
    if attack_card:
        lifesteal = attack_card.get_value(attack_card.charge)["lifesteal"]  # bool
        counter = attack_card.get_value(attack_card.charge)["counter"]  # bool
        if block_card:
            reflection = block_card.get_value(block_card.charge)["reflection"]  # bool
        if lifesteal:
            damage_1 = damage  # accessing the before calculated damage
            damage_2 = 0 - damage  # getting inflicted damage as health back
            if reflection:
                damage_1, damage_2 = damage_2, damage_1  # reflect shall reverse the lifesteal effect as well: an attack with lifesteal being reflected damages the attacker and adds health to the blocker
        elif not counter and reflection:  # no special effects but reflection
            damage_1 = 0  # no damage for the reflecting player
            damage_2 = damage  # all the damage for the attacking player
        else:  # if counter is active reflection is not relevant
            damage_1 = damage
            damage_2 = 0
    return damage_1, damage_2  # damage_1 changes blocker's health, damage_2 changes attacker's health // if positive life shall go down, if negative players shall gain health

def change_health(health_1, health_2, damage_1, damage_2):  # calculates new health based on warped damage
    new_health_1 = health_1 - damage_2
    new_health_2 = health_2 - damage_1
    return new_health_1, new_health_2

def full_combat_calc(attack_field, block_field, health_1, health_2, game_round):  # takes battling field pair and both health as input
    attack_card = separate_card(attack_field)  # gets attacking card
    block_card = separate_card(block_field)  # gets blocking card
    attack_value = set_calc_value(attack_card, "attack", game_round)
    block_value = set_calc_value(block_card, "block", game_round)
    damage = calc_dmg(attack_value, block_value)  # calculates damage between attacking and blocking card
    damage_1, damage_2 = warp_dmg(damage, attack_card, block_card)  # changes damage according to special effects (lifesteal, reflect, ...)
    new_health_1, new_health_2 = change_health(health_1, health_2, damage_1, damage_2)
    return new_health_1, new_health_2

def face_off_draw(draw_value_1, draw_value_2, card_1, card_2):
    block_draw_1 = card_1.get_value(card_1.charge)["block_draw"]  # bool
    steal_draw_1 = card_1.get_value(card_1.charge)["steal_draw"]  # bool
    counter_1 = card_1.get_value(card_1.charge)["counter"]  # bool

    block_draw_2 = card_2.get_value(card_2.charge)["block_draw"]  # bool
    steal_draw_2 = card_2.get_value(card_2.charge)["steal_draw"]  # bool
    counter_2 = card_2.get_value(card_2.charge)["counter"]  # bool

    special = [block_draw_1, steal_draw_1, block_draw_2, steal_draw_2]

    if any(special):
        if counter_1:  # N - F (any combination)
            draw_1 = draw_value_1 + 1
            draw_2 = 0
        elif counter_2:  # F - N (any combination)
            draw_1 = 0
            draw_2 = draw_value_2 + 1
        else:  # Group 2 & 4 - block/steal, no counter
            if block_draw_1:  # F (direct)
                if block_draw_2:  # F (direct) - F (direct)
                    draw_1 = 0
                    draw_2 = 0
                elif steal_draw_2:  # F (direct) - F (charged)
                    draw_1 = 0
                    draw_2 = draw_value_1
                else:  # F (direct) - any (normal, non-counter)
                    draw_1 = draw_value_1
                    draw_2 = 0
            elif steal_draw_1:  # F (charged)
                if block_draw_2:  # F (charged) - F (direct)
                    draw_1 = draw_value_2
                    draw_2 = 0
                elif steal_draw_2:  # F (charged) - F (charged)
                    draw_1 = draw_value_2
                    draw_2 = draw_value_1
                else:  # F (charged) - any (normal, non-counter)
                    draw_1 = draw_value_1 + draw_value_2
                    draw_2 = 0
            elif block_draw_2:  # any (normal, non-counter) - F (direct)
                draw_1 = 0
                draw_2 = draw_value_2
            else:  # any (normal, non-counter) - F (charged)
                draw_1 = 0
                draw_2 = draw_value_2 + draw_value_1
    else:  # Group 1 - normal
        draw_1 = draw_value_1
        draw_2 = draw_value_2
    return draw_1, draw_2

def warp_draw(draw_value_1, draw_value_2, card_1, card_2, game_round):
    if not card_1:
        if not card_2:
            draw_1, draw_2 = 0, 0
        else:
            draw_1 = 0
            draw_2 = draw_value_2
    else:
        if not card_2:
            draw_1 = draw_value_1
            draw_2 = 0
        else:
            if card_1.resolve == game_round:
                if card_2.resolve == game_round:
                    draw_1, draw_2 = face_off_draw(draw_value_1, draw_value_2, card_1, card_2)
                else:
                    draw_1 = draw_value_1
                    draw_2 = 0
            else:
                if card_2.resolve == game_round:
                    draw_1 = 0
                    draw_2 = draw_value_2
                else:
                    draw_1 = 0
                    draw_2 = 0
    return draw_1, draw_2

def full_draw_calc(draw_field_1, draw_field_2, zcr_bonus_1, zcr_bonus_2, game_round):
    card_1 = separate_card(draw_field_1)
    card_2 = separate_card(draw_field_2)
    draw_value_1 = set_calc_value(card_1, "draw", game_round)
    draw_value_2 = set_calc_value(card_2, "draw", game_round)
    draw_1, draw_2 = warp_draw(draw_value_1, draw_value_2, card_1, card_2, game_round)
    draw_1 = draw_1 + zcr_bonus_1
    draw_2 = draw_2 + zcr_bonus_2
    return draw_1, draw_2

def deduce_winner(player_1, player_2):
    if player_1.health <= 0 and player_2.health <= 0:
        winner = "no one"
    elif player_1.health <= 0:
        winner = player_2
    elif player_2.health <= 0:
        winner = player_1
    else:
        winner = None
    return winner

def game_end_message(winner):
    if winner == "no one":
        print("\nno one wins the game\nit's a draw")
    else:
        print(f"\n{winner.name} wins the game")


def main():
    perspective = "p1"
    board_width = 120
    game = Game()
    p1 = Player("ONE", BASIC_DECK, 13)
    p2 = Player("22222222", BASIC_DECK, 13)

    inter = Interface(p1, p2)
    inter.update_dict("game start", perspective, game.round)
    printer = Print(p1, p2, inter.p1_dict, inter.p2_dict)
    printer.print_game_board(game.round, "game start", board_width)

    player_list = [p1, p2]
    action_list = ["attack", "block", "draw"]

    for player in player_list:
        player.initial_deal(4)

    while True:
        game.round += 1

        for action in action_list:  # letting both players choose for each action before going to the next action
            inter.update_dict("play phase", perspective, game.round)
            printer = Print(p1, p2, inter.p1_dict, inter.p2_dict)
            printer.print_game_board(game.round, f"{action}", board_width)
            for player in player_list:
                player.play_card(action, game.round)

        inter.update_dict("end of action", perspective, game.round)
        printer = Print(p1, p2, inter.p1_dict, inter.p2_dict)
        printer.print_game_board(game.round, "end of action", board_width)
        p1.health, p2.health = full_combat_calc(p1.fields["attack"], p2.fields["block"], p1.health, p2.health, game.round)
        p2.health, p1.health = full_combat_calc(p2.fields["attack"], p1.fields["block"], p2.health, p1.health, game.round)

        input("\nreveal")

        inter.update_dict("reveal", perspective, game.round)
        printer = Print(p1, p2, inter.p1_dict, inter.p2_dict)
        printer.print_game_board(game.round, "reveal", board_width)
        winner = deduce_winner(p1, p2)
        if winner:
            game_end_message(winner)
            break

        zcr_1 = p1.zero_card_rule()
        zcr_2 = p2.zero_card_rule()
        draw_1, draw_2 = full_draw_calc(p1.fields["draw"], p2.fields["draw"], zcr_1, zcr_2, game.round)

        input("\nclean_up")
        p1.clean_up(game.round)
        p2.clean_up(game.round)

        input("\ndraw phase")
        overdraw_1 = p1.draw_cards(draw_1)
        print(f"\n{p1.name} draws: {draw_1} card(s)")
        print(f"overdraw_counter: {overdraw_1}")
        overdraw_2 = p2.draw_cards(draw_2)
        print(f"\n{p2.name} draws: {draw_2} card(s)")
        print(f"overdraw_counter: {overdraw_2}")
        input()

        inter.update_dict("end of round", perspective, game.round)
        printer = Print(p1, p2, inter.p1_dict, inter.p2_dict)
        printer.print_game_board(game.round, "end of round", board_width)

        input(f"\ncontinue for round: {game.round + 1}")


if __name__ == "__main__":
    main()
