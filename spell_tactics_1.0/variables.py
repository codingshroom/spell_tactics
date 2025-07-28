
# spell tactics // variables -------------------------------------------------------------------------------------------

game = True

rounds = 0  # in the first loop the game adds one. so we start with round 1
health_bot = 13
pre_calc_health_bot = 13

health_player = 13
pre_calc_health_player = 13

# deck of cards // discard pile // hands -------------------------------------------------------------------------------

deck_player = ["N", "A", "A", "P", "P", "F"]
deck_bot = ["N", "A", "A", "P", "P", "F"]

N_attack_direct = 1  # attack, block, draw values for N - direct and charged
N_block_direct = 1
N_draw_direct = 0
N_attack_charged = 2
N_block_charged = 2
N_draw_charged = 1

A_attack_direct = 2  # attack, block, draw values for A - direct and charged
A_block_direct = 2
A_draw_direct = 1
A_attack_charged = 4
A_block_charged = 3
A_draw_charged = 2

P_attack_direct = 3  # attack, block, draw values for P - direct and charged
P_block_direct = 3
P_draw_direct = 2
P_attack_charged = 6
P_block_charged = 4
P_draw_charged = 3

F_attack_direct = 0  # attack, block, draw values for F - direct and charged
F_block_direct = 0
F_draw_direct = 0
F_attack_charged = 4
F_block_charged = 0
F_draw_charged = 0

discard_pile_player = []  # where cards go before shuffled into the deck back again
discard_pile_bot = []

hand_player = []  # the cards player/bot see and can play
hand_bot = []

show_hand_bot = 0  # doesn't reveal background information - even if cards are put from hand_bot in reserve_fields

# fields // markers ----------------------------------------------------------------------------------------------------

attack_field_player = []  # where the cards are put and showcased
block_field_player = []
draw_field_player = []

attack_field_bot = []
block_field_bot = []
draw_field_bot = []

marker_bag = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]  # used to charge cards

go_back = False

# calculation structure ------------------------------------------------------------------------------------------------

heal_player = False  # attack_charged effect from 'F'
reflect_player = False  # block_charged effect from 'F'
block_draw_player = False  # draw_direct effect from 'F'
steal_draw_player = False  # draw_charged effect from 'F'
attack_player = 0  # raw attack value through attack field
block_player = 0  # raw block value through block field
calc_draw_player = 0  # raw draw value through draw field
zcr_player = 0  # value of zero card rule - if player has no cards in hand
draw_player = 0  # added value of raw draw and zero card rule

heal_bot = False
reflect_bot = False
block_draw_bot = False
steal_draw_bot = False
attack_bot = 0
block_bot = 0
calc_draw_bot = 0
zcr_bot = 0
draw_bot = 0

card_draw_count_player = 0  # showcase to player how many cards have actually been drawn
card_draw_count_bot = 0

shuffle_count_player = 0  # showcase to player if the discard pile got shuffled into the deck
shuffle_count_bot = 0

# bot protocol ---------------------------------------------------------------------------------------------------------

hundred = [1]  # percentage lists, hitting the 1 has a chance of ... percent
ninetyfive = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]
ninety = [1, 1, 1, 1, 1, 1, 1, 1, 1, 0]
eighty = [1, 1, 1, 1, 0]
seventy = [1, 1, 1, 1, 1, 1, 1, 0, 0, 0]
two_third = [1, 1, 0]
sixty = [1, 1, 1, 0, 0]
fifty = [0, 1]
fourty = [0, 0, 0, 1, 1]
one_third = [0, 0, 1]
thirty = [0, 0, 0, 0, 0, 0, 0, 1, 1, 1]
twenty = [0, 0, 0, 0, 1]
ten = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
five = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
zero = [0]

reserve_block = []  # lets bot put cards aside for block when block is more relevant than attacking
reserve_draw = []  # lets bot put cards aside for draw when draw is more relevant than attacking

attack_frenzy_system = False
afs_switch = 0  # int to determine whether attack_frenzy_system was activated in the round before
