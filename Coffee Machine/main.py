from logs import MENU, resources


PENNY = 0.01
NICKEL = 0.05
DIME = 0.10
QUARTER = 0.25


serve_coffee = True
while serve_coffee:
    prompt = str(input("What would you like? "
                       "(espresso/latte/cappuccino): ")).lower()
    machine_water = resources["water"]
    machine_milk = resources["milk"]
    machine_coffee = resources["coffee"]
    machine_money = resources["money"]

    def report_resources():
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${resources['money']}")


    def check_resources(coffee):
        if coffee == "cappuccino":
            if resources["water"] >= \
                    MENU["cappuccino"]["ingredients"]["water"] \
                    and resources["milk"] >= \
                    MENU["cappuccino"]["ingredients"]["milk"] and \
                    resources["coffee"] >= \
                    MENU["cappuccino"]["ingredients"]["coffee"]:
                return True
        elif coffee == "latte":
            if resources["water"] >= \
                    MENU["latte"]["ingredients"]["water"] \
                    and resources["milk"] >= \
                    MENU["latte"]["ingredients"]["milk"] and \
                    resources["coffee"] >= \
                    MENU["latte"]["ingredients"]["coffee"]:
                return True
        elif coffee == "espresso":
            if resources["water"] >= \
                    MENU["espresso"]["ingredients"]["water"] \
                    and resources["coffee"] >= \
                    MENU["espresso"]["ingredients"]["coffee"]:
                return True
        else:
            return False


    def pay_total():
        input_quarter = float(input("How many quarters?: ")) * QUARTER
        input_dime = float(input("How many dimes?: ")) * DIME
        input_nickel = float(input("How many nickels?: ")) * NICKEL
        input_penny = float(input("How many pennies?: ")) * PENNY
        total = input_penny + input_nickel + input_dime + input_quarter
        return total

    def sufficient_money(pay_total):
        if prompt == "cappuccino" and pay_total >= 3:
            change = pay_total - 3
            return change
        elif prompt == "latte" and pay_total >= 2.5:
            change = pay_total - 2.5
            return change
        elif prompt == "espresso" and pay_total >= 1.5:
            change = pay_total - 1.5
            return change
        else:
            return False

    enough_resources = check_resources(prompt)
    if enough_resources:
        print("Please insert coins")
        pay_total = pay_total()
        change = sufficient_money(pay_total)
        if change > 0:
            add_money_to_machine = pay_total - float(change)
            resources["money"] += add_money_to_machine
            print(f"Here is ${round(float(change), 3)} in change.")
            print(f"Here is your {prompt}. Enjoy")
            if prompt == "cappuccino":
                resources["milk"] -= 100
                resources["water"] -= 250
                resources["coffee"] -= 24
            elif prompt == "latte":
                resources["milk"] -= 150
                resources["water"] -= 200
                resources["coffee"] -= 24
            elif prompt == "espresso":
                resources["water"] -= 50
                resources["coffee"] -= 18
        elif not change:
            print("Sorry that's not enough money. Money refunded.")
    elif not enough_resources:
        print("Sorry this machine doesn't have enough "
              "coffee/milk/water. Try again later")
        serve_coffee = False

    if prompt == "report":
        report_resources()
    elif prompt == "exit":
        print("Shutting down...")
        serve_coffee = False

