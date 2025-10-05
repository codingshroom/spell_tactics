
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

