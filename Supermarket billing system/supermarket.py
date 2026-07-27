import json
from product import Product


class Supermarket:
    def __init__(self):
        self.__products = []
        self.__cart = []
        self.load_products()

    def load_products(self):
        try:
            with open("products.json", "r") as file:
                data = json.load(file)

                for item in data:
                    self.__products.append(
                        Product(item["id"], item["name"], item["price"])
                    )

        except FileNotFoundError:
            pass

    def save_products(self):
        data = []

        for product in self.__products:
            data.append({
                "id": product.get_id(),
                "name": product.get_name(),
                "price": product.get_price()
            })

        with open("products.json", "w") as file:
            json.dump(data, file, indent=4)

    def add_product(self, pid, name, price):
        product = Product(pid, name, price)
        self.__products.append(product)
        self.save_products()
        print("Product added successfully!")

    def view_products(self):
        if not self.__products:
            print("No products available.")
            return

        print("\n===== PRODUCTS =====")

        for product in self.__products:
            product.display()

    def add_to_cart(self, pid, qty):
        for product in self.__products:
            if product.get_id() == pid:
                self.__cart.append((product, int(qty)))
                print("Added to cart!")
                return

        print("Product not found!")

    def generate_bill(self):
        if not self.__cart:
            print("Cart is empty.")
            return

        subtotal = 0

        print("\n========== BILL ==========")

        for product, qty in self.__cart:
            total = product.get_price() * qty
            subtotal += total

            print(f"{product.get_name()} x{qty} = Rs. {total}")

        discount = subtotal * 0.10 if subtotal >= 5000 else 0
        tax = (subtotal - discount) * 0.13
        final = subtotal - discount + tax

        print("----------------------------")
        print(f"Subtotal : Rs. {subtotal}")
        print(f"Discount : Rs. {discount}")
        print(f"VAT (13%): Rs. {tax}")
        print(f"Total    : Rs. {final}")

        self.__cart.clear()