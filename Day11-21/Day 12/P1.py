import os
os.system('cls')
## Scope##
ENEMIES = 1


def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {ENEMIES}")

## local scope##
# def drick_poition():
#     potion_strength = 2
#     print(potion_strength)

# drick_poition()

## Global Scope##
player_health = 10


def game():
    def drick_poition():
        potion_strength = 2
        print(player_health)
    drick_poition()
