"""Module for screen clear"""
import os
from p2_resources import MENU
from p2_resources import recursos
os.system('cls')

RESOURCES = recursos
coffee_menu = MENU

PROFIT = 0

def value_coffee():#Segunda funcion que se llama
    '''This funcion return the value of the coffee'''
    coffee_espresso = coffee_menu[select_coffee]
    latte_cost = coffee_espresso["cost"]
    return latte_cost
# coffe_value_variable = value_coffee()

def rest_coffee(order_ingredients):#primera funcion que se llama
    '''This funcion return the value of the coffee'''
    for item in order_ingredients:
        RESOURCES[item] -= order_ingredients[item]

def make_coffee(order_ingredients):
    ''''Evaluates if the coffee can be made'''
    for item in order_ingredients:
        if RESOURCES[item] < order_ingredients[item]:
            print((f"Sorry there is not enough {item}."))
            return False
        return True

def sum_coins():#Tercera funcion que se llama
    '''It makes the sum of the coins'''
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def pay_change():#Cuarta funcion que se llama
    '''Evaluates the amount of money and give back the change'''
    suma_total = sum_coins()
    if coffe_value_variable == suma_total:
        return f"Here is your {select_coffee} ☕️. Enjoy!"
    elif coffe_value_variable < suma_total:
        change_pay_value = suma_total - coffe_value_variable
        change_pay_value = round(change_pay_value, 3)
        return f"Here is ${change_pay_value} in change.\nHere is your {select_coffee} ☕️. Enjoy!"
    elif coffe_value_variable > suma_total:
        print("Sorry that's not enough money. Money refunded.")
        return False

ON_COFFEE_MACHINE = True
while ON_COFFEE_MACHINE:
    select_coffee = input("What would you like? (espresso/latte/cappuccino): ")
    if select_coffee == "off":
        ON_COFFEE_MACHINE = False
    elif select_coffee == "report":
        print(f"Water: {RESOURCES['water']}ml")
        print(f"Milk: {RESOURCES['milk']}ml")
        print(f"Coffee: {RESOURCES['coffee']}g")
        print(f"Money: ${PROFIT}")
    else:
        drink = coffee_menu[select_coffee]
        if make_coffee(drink["ingredients"]):
            rest_coffee(drink["ingredients"])
            coffe_value_variable = value_coffee()
            PROFIT += coffe_value_variable
            print(pay_change())
