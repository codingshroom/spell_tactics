# trying with variables and return statements. keeping things clean.

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
        self.end = False
        self.round = 0

    @staticmethod
    def overview(moment):
        print(f"\n\n---------- round: {game.round} ---------- {moment} ----------\n")

        zones_dict_1 = {"deck": p1.deck, "hand": p1.hand, "attack": p1.attack_field, "block": p1.block_field,
                        "draw": p1.draw_field, "discard": p1.discard}
        zones_dict_2 = {"deck": p2.deck, "hand": p2.hand, "attack": p2.attack_field, "block": p2.block_field,
                        "draw": p2.draw_field, "discard": p2.discard}

        print(f"{p1.name}: ")
        print(f"health:".ljust(11, " "), p1.health)
        for zone in zones_dict_1:
            print(f"{zone}:".ljust(12, " "), end=""), print_cards(zones_dict_1.get(zone))

        print(f"\n{p2.name}: ")
        print(f"health:".ljust(11, " "), p2.health)
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


class Player:
    def __init__(self, name, deck):
        self.name = name
        self.health = 13
        self.card_dict = {name: Card(name, data) for name, data in deck.items()}  # mapping card.name to card objects
        self.deck = list(self.card_dict.values())  # adding each created card to deck
        random.shuffle(self.deck)  # randomizing order
        self.hand = []
        self.attack_field = []
        self.block_field = []
        self.draw_field = []
        self.discard = []
        self.field_list = [self.attack_field, self.block_field, self.draw_field]
        self.zone_list = [self.deck, self.hand, self.attack_field, self.block_field, self.draw_field, self.discard]

    @staticmethod
    def initial_deal(deck, hand):  # dealing four cards
        new_deck = deck.copy()
        new_hand = hand.copy()
        for i in range(4):
            card = new_deck[0]
            new_deck.remove(card)
            new_hand.append(card)
        return new_deck, new_hand

    def select_card(self, hand, action):  # player picks a card from their hand
        if hand:
            while True:  # looping until: card from hand or skip ("0")
                card_name = input(f"\n{self.name} pick a card for {action}: ").upper()
                if card_name == "0":
                    return None
                card = self.card_dict.get(card_name)  # getting card object
                if card in hand:  # checking validity of play
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

    @staticmethod
    def update_card(card, mode):  # saving information of charge in card itself
        if mode == "C":  # charged
            card.charge = "charged"
            card.resolve = game.round + 1  # resolve should happen in the following round
        elif mode == "D":  # directly played
            card.charge = "direct"
            card.resolve = game.round  # resolve should happen in this round
        return card

    @staticmethod
    def new_hand(hand, card):  # updating hand to (hand - card)
        new_hand = hand.copy()
        if card is not None:
            new_hand.remove(card)
            return new_hand
        return hand

    @staticmethod
    def new_field(field, card):  # updating field to field + card
        new_field = field.copy()
        if card is not None:
            new_field.append(card)
            return new_field
        return field

    def play_card(self, hand, field, action):  # putting a card from players hand to the field with/-out charge
        if field:  # not allowing play if the field has a card already
            input(f"\nyou already played {action}")
        else:
            card = self.select_card(hand, action)  # picking card
            mode = self.select_mode(card)  # picking mode: charged or direct
            card = self.update_card(card, mode)  # changing attributes of selected card
            new_hand = self.new_hand(hand, card)  # updating hand
            new_field = self.new_field(field, card)  # updating field
            if new_hand is not None and new_field is not None:
                return new_hand, new_field
        return hand, field

    @staticmethod
    def draw_cards(deck, hand, discard, card_amount):
        new_deck = deck.copy()
        new_hand = hand.copy()
        new_discard = discard.copy()
        overdraw_counter = 0
        if card_amount == 0:
            pass
        else:
            draw_flat = min(len(new_deck), card_amount)
            draw_shuffle = max(card_amount - len(new_deck), 0)
            for i in range(draw_flat):
                if new_deck:
                    card = new_deck[0]
                    new_deck.remove(card)
                    new_hand.append(card)
                else:
                    overdraw_counter += 1
            if draw_shuffle >= 1:
                new_deck, new_discard = shuffle(new_deck, new_discard)
                for i in range(draw_shuffle):
                    if new_deck:
                        card = new_deck[0]
                        new_deck.remove(card)
                        new_hand.append(card)
                    else:
                        overdraw_counter += 1
        print(f"overdraw_counter: {overdraw_counter}")
        return new_deck, new_hand, new_discard, overdraw_counter


def shuffle(deck, discard):
    new_deck = deck.copy()
    new_discard = discard.copy()
    for i in range(len(new_discard)):
        card = new_discard[0]
        new_deck.append(card)
        new_discard.remove(card)
    random.shuffle(new_deck)
    return new_deck, new_discard


def separate(field):  # getting card object from field
    if field:
        card = field[0]
    else:
        card = None
    return card


def set_calc_value(card, field):
    value = 0
    if card:
        if card.resolve == game.round:  # checking if card should be resolved this round
            if card.charge == "charged":  # checking charge of card
                value = card.get_value("charged")[field]  # accessing charged value of card in field
            else:
                value = card.get_value("direct")[field]  # accessing direct value of card in field
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
    return damage_1, damage_2  # damage_1 changes blocker's health, damage_2 changes attacker's health // if positive life shall go down, if negative players shall be healed


def change_health(health_1, health_2, damage_1, damage_2):  # calculates new health based on warped damage
    new_health_1 = health_1 - damage_2
    new_health_2 = health_2 - damage_1
    return new_health_1, new_health_2


def full_combat_calc(attack_field, block_field, health_1, health_2):  # takes fields and both health as input
    attack_card = separate(attack_field)
    block_card = separate(block_field)
    attack_value = set_calc_value(attack_card, "attack")
    block_value = set_calc_value(block_card, "block")
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


def warp_draw(draw_value_1, draw_value_2, card_1, card_2):
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
            if card_1.resolve == game.round:
                if card_2.resolve == game.round:
                    draw_1, draw_2 = face_off_draw(draw_value_1, draw_value_2, card_1, card_2)
                else:
                    draw_1 = draw_value_1
                    draw_2 = 0
            else:
                if card_2.resolve == game.round:
                    draw_1 = 0
                    draw_2 = draw_value_2
                else:
                    draw_1 = 0
                    draw_2 = 0
    return draw_1, draw_2


def zero_card_rule(hand, health):
    if hand:
        zcr_bonus = 0
    else:
        if health <= 3:
            zcr_bonus = 2
        else:
            zcr_bonus = 1
    return zcr_bonus


def full_draw_calc(draw_field_1, draw_field_2):
    card_1 = separate(draw_field_1)
    card_2 = separate(draw_field_2)
    draw_value_1 = set_calc_value(card_1, "draw")
    draw_value_2 = set_calc_value(card_2, "draw")
    draw_1, draw_2 = warp_draw(draw_value_1, draw_value_2, card_1, card_2)
    draw_1 = draw_1 + zero_card_rule(p1.hand, p1.health)
    draw_2 = draw_2 + zero_card_rule(p2.hand, p2.health)
    return draw_1, draw_2


def clean_up(field, discard):
    new_field = field.copy()
    new_discard = discard.copy()
    if field:
        card = field[0]
        if card.resolve == game.round:
            Player.update_card(card, "direct")
            new_field.remove(card)
            new_discard.append(card)
    return new_field, new_discard



game = Game()
p1 = Player("ONE", BASIC_DECK)
p2 = Player("22222222", BASIC_DECK)



def main():
    game.overview("game start")

    p1.deck, p1.hand = p1.initial_deal(p1.deck, p1.hand)
    p2.deck, p2.hand = p2.initial_deal(p2.deck, p2.hand)

    while True:
        game.round += 1
        game.overview("play phase: attack")
        p1.hand, p1.attack_field = p1.play_card(p1.hand, p1.attack_field, "attack")
        p2.hand, p2.attack_field = p2.play_card(p2.hand, p2.attack_field, "attack")

        game.overview("play phase: block")
        p1.hand, p1.block_field = p1.play_card(p1.hand, p1.block_field, "block")
        p2.hand, p2.block_field = p2.play_card(p2.hand, p2.block_field, "block")

        game.overview("play phase: draw")
        p1.hand, p1.draw_field = p1.play_card(p1.hand, p1.draw_field, "draw")
        p2.hand, p2.draw_field = p2.play_card(p2.hand, p2.draw_field, "draw")

        game.overview("calculations")
        p1.health, p2.health = full_combat_calc(p1.attack_field, p2.block_field, p1.health, p2.health)
        p2.health, p1.health = full_combat_calc(p2.attack_field, p1.block_field, p2.health, p1.health)

        draw_1, draw_2 = full_draw_calc(p1.draw_field, p2.draw_field)

        input("\nclean_up")
        p1.attack_field, p1.discard = clean_up(p1.attack_field, p1.discard)
        p1.block_field, p1.discard = clean_up(p1.block_field, p1.discard)
        p1.draw_field, p1.discard = clean_up(p1.draw_field, p1.discard)

        p2.attack_field, p2.discard = clean_up(p2.attack_field, p2.discard)
        p2.block_field, p2.discard = clean_up(p2.block_field, p2.discard)
        p2.draw_field, p2.discard = clean_up(p2.draw_field, p2.discard)


        game.overview("draw")
        input("\ndraw phase")

        print(f"\n{p1.name} draws: {draw_1} card(s)")
        p1.deck, p1.hand, p1.discard, overdraw_1 = p1.draw_cards(p1.deck, p1.hand, p1.discard, draw_1)
        print(f"\n{p2.name} draws: {draw_2} card(s)")
        p2.deck, p2.hand, p2.discard, overdraw_2 = p2.draw_cards(p2.deck, p2.hand, p2.discard, draw_2)

        game.overview("round finished")
        input(f"\ncontinue for round: {game.round + 1}")


if __name__ == "__main__":
    main()
