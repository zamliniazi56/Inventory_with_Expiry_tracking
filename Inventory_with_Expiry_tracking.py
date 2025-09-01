
from datetime import datetime
inventory = []

def add():
    while True:
        try:
            name = input("Enter product name: ")
            qty = int(input("Enter quantity of a product: "))
            expiry = input("Enter expiry date of product (YYYY-MM-DD): ")

            try:
                datetime.strptime(expiry, "%Y-%m-%d")
            except ValueError:
                print("Bhai patteren follow kro...")
                continue

            products = {

                    "name": name,
                    "quantity": qty,
                    "expiry": expiry
            }

            inventory.append(products)
            print("product added in inventory")

            new_1 = input("\nyou want to add another product (yes/no): ")
            if new_1 == "yes":
               add()

            else:
               print("okie nikl....")
            break

        except ValueError:
             print("value error! try again...")

def show():
    print("\n.....Inventory.....\n")
    for i in inventory:
        print(f"name:{i["name"]}, quantity:{i["quantity"]}, expiry:{i["expiry"]}")

def sell():
        try:
            name = input("Enter product you want to sell: ")
            qty = int(input("Enter quantity of product you want to sell: "))
            product_found = False

            for i in inventory:
                if i["name"] == name:
                    product_found = True
                    if int(i["quantity"]) >= qty:
                        i["quantity"] = int(i["quantity"]) - qty
                        print("sell successfully..")
                        if i["quantity"] == 0:
                            inventory.remove(i)
                            print("product removed...(out of stock)")
                            break
                    else:
                        print("not enough (stock)....")
                        break

            if not product_found:
                print("product not available...")

            new = input("\nyou want to sell another product (yes/no): ")
            if new == "yes":
                sell()
            else:
                print("okie nikl...")

        except ValueError:
            print("value error..try again!")

def show_expiry():

    name = input("Enter product to check is it expire or not : ")
    now = datetime.now().date()
    product_found = False

    for i in inventory:
        if i["name"] == name:
           product_found = True
           expiry_date = datetime.strptime(i["expiry"], "%Y-%m-%d").date()

           if now > expiry_date:

                print(f"{i["name"]} is expired..")
                inventory.remove(i)
                print(f"{i["name"]} is now removed...")

           elif (expiry_date - now).days <= 7:

                print(f"{i["name"]} is near to expired.{(expiry_date - now).days},days left...")
           else:
                print(f"{i["name"]} is ok! for now...")

    if not product_found:
        print("product not found...")

def main():

    print("\n.......WELLCOME........")

    while True:
        choice = input("\nyou want to (add/sell/show/expiry_status/exit) product: ")

        if choice == "add":
            add()
        elif choice == "sell":
            sell()
        elif choice == "show":
            show()
        elif choice == "expiry_status":
            show_expiry()
        elif choice == "exit":
            print("Thanks for using our system")
            exit()
        else:
            print("Bhai invalid choice..!! TRY AGAIN.")
main()






