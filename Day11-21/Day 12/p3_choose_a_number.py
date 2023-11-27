'''
Something that describes the module.
'''
import os
import random
os.system('cls')

print("Welcome to the number guessing game!")


def choose_number():
    """Definir un numero random para el juego"""
    lista = [1]
    for i in lista:
        lista.append(i+1)
        if i == 99:
            break
    # print (list)
    return random.choice(lista)


def easy():
    """Funcion del nivel facil del juego"""
    easy_attempts = 10
    print("You have 10 attempts remaining to guess the number.")
    while easy_attempts > 0:
        easy_guess = int(input("Make a guess: "))
        if easy_guess == number_random:
            print(f"You got it! The answer was {easy_guess}.")
            easy_attempts = 0
        elif easy_guess > number_random:
            print("Too high")
            easy_attempts -= 1
            if easy_attempts > 0:
                print(
                    f"Guess again\nYou have {easy_attempts} attempts remaining to guess the number")
            else:
                print(
                    f"You've run out of guesses, you lose. The rigth answer was {number_random}")
        else:
            print("Too low")
            easy_attempts -= 1
            if easy_attempts > 0:
                print(
                    f"Guess again\nYou have {easy_attempts} attempts remaining to guess the number")
            else:
                print("You've run out of guesses, you lose.")


def hard():
    """Funcion del nivel dificil del juego"""
    hard_attempts = 5
    print("You have 5 attempts remaining to guess the number.")
    while hard_attempts > 0:
        hard_guess = int(input("Make a guess: "))
        if hard_guess == number_random:
            print(f"You got it! The answer was {hard_guess}.")
            hard_attempts = 0
        elif hard_guess > number_random:
            print("Too high")
            hard_attempts -= 1
            if hard_attempts > 0:
                print(
                    f"Guess again\nYou have {hard_attempts} attempts remaining to guess the number")
            else:
                print("You've run out of guesses, you lose.")
        else:
            print("Too low")
            hard_attempts -= 1
            if hard_attempts > 0:
                print(
                    f"Guess again\nYou have {hard_attempts} attempts remaining to guess the number")
            else:
                print(
                    f"You've run out of guesses, you lose. The rigth answer was {number_random}")


def terminar():
    """Funcion para terminar o continuar el juego"""
    seguir_cerrar = input(
        "\nIf you want to try again type 'yes' and if you want to close type 'no': ")
    if seguir_cerrar == "yes":
        return True
    else:
        return False


HOLA = True
while HOLA:
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    number_random = choose_number()
    # print(f"Psss this is the number to guess: {number_random}")
    if level == "easy":
        easy()
        HOLA = terminar()
        os.system('cls')
    elif level == "hard":
        hard()
        HOLA = terminar()
        os.system('cls')
    else:
        HOLA = terminar()
        os.system('cls')
