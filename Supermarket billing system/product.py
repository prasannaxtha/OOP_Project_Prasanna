class Product:
    def __init__(self, product_id, name, price):
        self.__product_id = product_id
        self.__name = name
        self.__price = float(price)

    def get_id(self):
        return self.__product_id

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def display(self):
        print(f"{self.__product_id} | {self.__name} | Rs. {self.__price}")