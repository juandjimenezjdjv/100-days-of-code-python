"""Modulo para limpiar"""
import os
import random
from p4_people_compare import data
import p5_logo

os.system('cls')


def random_user_selector():
    '''funcion that give us the position of a user'''
    seleb_busc = random.choice(data)
    contador = 0
    for i in data:
        if i != seleb_busc:
            contador += 1
        if i == seleb_busc:
            break
    return contador


def user_description():
    """Helps to give all the data from the users"""
    # print(people_data)
    rand_name = people_data["name"]
    rand_descrip = people_data["description"]
    rand_count = people_data["country"]
    return f" {rand_name}, {rand_descrip}, from {rand_count}."

# These give us the data from the first person #
USER_POSITION = random_user_selector()
people_data = data[USER_POSITION]
RAND_FOLLOWER_1 = people_data['follower_count']
person_1 = user_description()


PLAY_GAME = True
GAME_POINTS = 0
while PLAY_GAME:
    DO_YOU_WANT_FINISH = True
    print(f"{p5_logo.LOGO}")
    print(f"Your actual score is: {GAME_POINTS}")
    print(f"Compare A:{person_1}")
    print(f"{p5_logo.VS}")

    USER_POSITION = random_user_selector()
    people_data = data[USER_POSITION]

    RAND_FOLLOWER_2 = people_data['follower_count']
    person_2 = user_description()
    print(f"Against B:{person_2}")

    FOLLOWER_COMPARE = input(
        "\nWho has more followers? Type 'A' or 'B': ").upper()

    if RAND_FOLLOWER_1 == RAND_FOLLOWER_2:
        PLAY_GAME = True
        os.system('cls')
    elif RAND_FOLLOWER_1 > RAND_FOLLOWER_2:
        if FOLLOWER_COMPARE == "A":
            GAME_POINTS += 1
            os.system('cls')
            person_1 = person_2
        elif FOLLOWER_COMPARE == "B":
            DO_YOU_WANT_FINISH = False
            print(f"\nYour score was {GAME_POINTS}")
    elif RAND_FOLLOWER_1 < RAND_FOLLOWER_2:
        if FOLLOWER_COMPARE == "A":
            DO_YOU_WANT_FINISH = False
            print(f"\nYour score was {GAME_POINTS}")
        elif FOLLOWER_COMPARE == "B":
            GAME_POINTS += 1
            os.system('cls')
            person_1 = person_2
    

    # Aqui hacer un IF para que si el juego termina aparesca lo de aabjo
    # y sino que el juego siga sin que aparesca.
    if DO_YOU_WANT_FINISH is False:
        # print(f"Your score was {GAME_POINTS}\n")
        try_again_end_game = input(
            "\nIf you want to play again type 'yes' or if you want to finish type 'no': ")
        if try_again_end_game == "yes":
            PLAY_GAME = True
            os.system('cls')
            GAME_POINTS = 0
        elif try_again_end_game == "no":
            PLAY_GAME = False
        else:
            print("Since you didn't choose correctly, the game has close'")
            PLAY_GAME = False
