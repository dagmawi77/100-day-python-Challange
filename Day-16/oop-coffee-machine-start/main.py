from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

menu = Menu()
is_on = True


while is_on:
    option = menu.get_items()
    choies = input(f"What would You like ({option})").lower()

    if(choies == "off"):
        is_on = False
    elif choies == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choies)
        print(drink)