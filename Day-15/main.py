
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
profite = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}




quarters = 0.25
dimes = 0.10
nickles = 0.05
pennies = 0.01

game_countinue = True
while game_countinue:
    user_choies = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_choies == "off":
        print("Game Over")
        game_countinue = False
    elif user_choies == "report":
        for index in resources:
            print(f"{index} : {resources[index]}")
        print(f"Money : {profite} ")
#         print(f"Water : {resources['water']}")
#         print(f"Milk : {resources['milk']} " )
#         print(f"Coffee : {resources['coffee']} ")
#         print(f"Money : {profite} ")
    elif user_choies == "espresso" or user_choies == "latte" or user_choies == "cappuccino":
        print("please Enter Coin.")
        quarters_value = int(input("How many quarters? : "))
        dimes_value = int(input("How many dimes? : "))
        nickles_value = int(input("How many nickles? : "))
        pennies_value = int(input("How many quarters? : "))


        change = (quarters * quarters_value) + (dimes * dimes_value) + (nickles * nickles_value) + (pennies * pennies_value)
        print(f"here is change ${(change)}")
