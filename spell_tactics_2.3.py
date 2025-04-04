# functions with clear input(arguments) + output(return statements)
# using strengths of Classes, manipulating fields & cards directly in Player object

import random

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


def print_cards(zone):  # help function for printing cards in zones
    if zone:  # checking if cards in zone
        card_info = [f"{card.name} {card.charge, card.resolve}" for card in zone if
                     card is not None]  # compiling list with card name, charge, resolve information
        return print(", ".join(card_info))
    print("")


class Game:
    def __init__(self):
        self.round = 0

    @staticmethod
    def overview(moment, player_1, player_2, game_round):
        print(f"\n\n---------- round: {game_round} ---------- {moment} ----------\n")

        zones_dict_1 = {"deck": player_1.deck, "hand": player_1.hand, "attack": player_1.fields["attack"], "block": player_1.fields["block"],
                        "draw": player_1.fields["draw"], "discard": player_1.discard}
        zones_dict_2 = {"deck": player_2.deck, "hand": player_2.hand, "attack": player_2.fields["attack"], "block": player_2.fields["block"],
                        "draw": player_2.fields["draw"], "discard": player_2.discard}

        print(f"{player_1.name}: ")
        print(f"health:".ljust(11, " "), player_1.health)
        for zone in zones_dict_1:
            print(f"{zone}:".ljust(12, " "), end=""), print_cards(zones_dict_1.get(zone))

        print(f"\n{player_2.name}: ")
        print(f"health:".ljust(11, " "), player_2.health)
        for zone in zones_dict_2:
            print(f"{zone}:".ljust(12, " "), end=""), print_cards(zones_dict_2.get(zone))


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
    def __init__(self, name, deck):
        self.name = name
        self.health = 13
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
                print("choose a valid option")

    def new_hand(self, card):  # updating hand to (hand - card)
        if card is not None:
            self.hand.remove(card)

    def new_field(self, action, card):  # updating field to field + card
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
        if card_amount == 0:
            pass
        else:
            draw_flat = min(len(self.deck), card_amount)  # amount of cards that player can draw from his current deck
            draw_shuffle = max(card_amount - len(self.deck), 0)  # amount of cards that player will draw from his deck after it has been shuffled
            for i in range(draw_flat):
                if self.deck:
                    card = self.deck[0]
                    self.deck.remove(card)
                    self.hand.append(card)
                else:
                    overdraw_counter += 1
            if draw_shuffle >= 1:
                self.shuffle()
                for i in range(draw_shuffle):
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

    def zero_card_rule(self):
        if self.hand:
            zcr_bonus = 0
        else:
            if self.health <= 3:
                zcr_bonus = 2
            else:
                zcr_bonus = 1
        return zcr_bonus


def separate(field):  # getting card object from field
    if field:
        card = field[0]
    else:
        card = None
    return card


def set_calc_value(card, action, game_round):
    value = 0
    if card:
        if card.resolve == game_round:  # checking if card should be resolved this round
            if card.charge == "charged":  # checking charge of card
                value = card.get_value("charged")[action]  # accessing charged value of card in field
            else:
                value = card.get_value("direct")[action]  # accessing direct value of card in field
    return value


def calc_dmg(attack_value, block_value):
    damage = max(0, attack_value - block_value)  # calculating damage, not allowing negative
    return damage


def warp_dmg(damage, attack_card, block_card):
    damage_1, damage_2 = 0, 0
    reflection = False
    if attack_card:
        lifesteal = attack_card.get_value(attack_card.charge)["lifesteal"]  # outputs True/False
        counter = attack_card.get_value(attack_card.charge)["counter"]  # outputs True/False
        if block_card:
            reflection = block_card.get_value(block_card.charge)["reflection"]  # outputs True/False
        if lifesteal:
            damage_1 = damage  # accessing the before calculated damage
            damage_2 = 0 - damage  # getting inflicted damage as health back
            if reflection:
                damage_1, damage_2 = damage_2, damage_1  # reflect shall reverse the lifesteal effect as well: so an attack with lifesteal being reflected damages the attacker and adds health to the blocker
        elif not counter and reflection:
            damage_1 = 0
            damage_2 = damage
        else:  # if counter is active reflection is not relevant
            damage_1 = damage
            damage_2 = 0
    return damage_1, damage_2  # damage_1 changes blocker's health, damage_2 changes attacker's health // if positive life shall go down, if negative players shall gain health


def change_health(health_1, health_2, damage_1, damage_2):  # calculates new health based on warped damage
    new_health_1 = health_1 - damage_2
    new_health_2 = health_2 - damage_1
    return new_health_1, new_health_2


def full_combat_calc(attack_field, block_field, health_1, health_2, game_round):  # takes fields and both health as input
    attack_card = separate(attack_field)
    block_card = separate(block_field)
    attack_value = set_calc_value(attack_card, "attack", game_round)
    block_value = set_calc_value(block_card, "block", game_round)
    damage = calc_dmg(attack_value, block_value)
    damage_1, damage_2 = warp_dmg(damage, attack_card, block_card)
    new_health_1, new_health_2 = change_health(health_1, health_2, damage_1, damage_2)
    return new_health_1, new_health_2


def face_off_draw(draw_value_1, draw_value_2, card_1, card_2):
    block_draw_1 = card_1.get_value(card_1.charge)["block_draw"]  # True/False
    steal_draw_1 = card_1.get_value(card_1.charge)["steal_draw"]  # True/False
    counter_1 = card_1.get_value(card_1.charge)["counter"]  # True/False

    block_draw_2 = card_2.get_value(card_2.charge)["block_draw"]  # True/False
    steal_draw_2 = card_2.get_value(card_2.charge)["steal_draw"]  # True/False
    counter_2 = card_2.get_value(card_2.charge)["counter"]  # True/False

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
    card_1 = separate(draw_field_1)
    card_2 = separate(draw_field_2)
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
    game = Game()
    p1 = Player("ONE", BASIC_DECK)
    p2 = Player("22222222", BASIC_DECK)
    game.overview("game start", p1, p2, game.round)

    player_list = [p1, p2]
    action_list = ["attack", "block", "draw"]

    for player in player_list:
        player.initial_deal(3)

    while True:
        game.round += 1

        for action in action_list:  # letting both players choose for each action before going to the next action
            game.overview(f"play phase: {action}", p1, p2, game.round)
            for player in player_list:
                player.play_card(action, game.round)

        game.overview("end of actions", p1, p2, game.round)
        p1.health, p2.health = full_combat_calc(p1.fields["attack"], p2.fields["block"], p1.health, p2.health, game.round)
        p2.health, p1.health = full_combat_calc(p2.fields["attack"], p1.fields["block"], p2.health, p1.health, game.round)

        game.overview("reveal", p1, p2, game.round)
        winner = deduce_winner(p1, p2)
        if winner:
            game_end_message(winner)
            break

        zcr_1 = p1.zero_card_rule()
        zcr_2 = p2.zero_card_rule()
        draw_1, draw_2 = full_draw_calc(p1.fields["draw"], p2.fields["draw"], zcr_1, zcr_2, game.round)

        game.overview("calculations", p1, p2, game.round)

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

        game.overview("round finished", p1, p2, game.round)
        input(f"\ncontinue for round: {game.round + 1}")


if __name__ == "__main__":
    main()
