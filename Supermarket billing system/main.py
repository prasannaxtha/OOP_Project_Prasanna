from supermarket import Supermarket


def menu():

    market = Supermarket()

    while True:

        print("\n" + "=" * 40)
        print("    SUPERMARKET BILLING SYSTEM")
        print("=" * 40)
        print("1. Add Product")
        print("2. View Products")
        print("3. Add To Cart")
        print("4. Generate Bill")
        print("5. Exit")

        choice = input("Enter your choice: ")

        try:

            if choice == "1":

                pid = input("Product ID: ")
                name = input("Product Name: ")
                price = float(input("Price: "))

                market.add_product(pid, name, price)

            elif choice == "2":

                market.view_products()

            elif choice == "3":

                pid = input("Product ID: ")
                qty = int(input("Quantity: "))

                market.add_to_cart(pid, qty)

            elif choice == "4":

                market.generate_bill()

            elif choice == "5":

                print("Thank you!")
                break

            else:

                print("Invalid choice!")

        except ValueError:

            print("Invalid input! Please enter numeric values for price and quantity.")


if __name__ == "__main__":
    menu()