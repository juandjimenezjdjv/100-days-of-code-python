'''
Modulo para limpiar pantalla
'''
import os
os.system('cls')

# number = int(input("Which number do you want to check?"))

# if number % 2 == 0:
#     print("This is an even number.")
# else:
#     print("This is an odd number.")

for number in range(0, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(f"{number}")
