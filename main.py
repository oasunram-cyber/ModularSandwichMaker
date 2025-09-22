import data
from sandwich_maker import SandwichMaker
from cashier import Cashier

resources = data.resources.copy()
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()


def main():
    is_on = True

    while is_on:
        choice = input("What would you like? (small/medium/large) or 'report' or 'off': ").lower()

        if choice == "off":
            is_on = False
            print("Turning off the machine. Goodbye!")
        elif choice == "report":
            print("\nMachine Resources:")
            for item, amount in resources.items():
                print(f"{item}: {amount}")
            print("")
        elif choice in recipes:
            order = recipes[choice]
            cost = order["cost"]
            print(f"The {choice} sandwich costs ${cost}.")

            if sandwich_maker_instance.check_resources(order["ingredients"]):
                payment = cashier_instance.process_coins()
                if cashier_instance.transaction_result(payment, cost):
                    sandwich_maker_instance.make_sandwich(choice, order["ingredients"])
        else:
            print("Invalid choice. Please select small, medium, or large.")


if __name__ == "__main__":
    main()
