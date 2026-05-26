class Product:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def get_price(self):
        return self.__price

    def get_info(self):
        return f" товар: {self.__name}, цена: {self.__price} рублей"
    
class Vegetable(Product):
    def __init__(self, name, price, weight):
        super().__init__(name, price)
        self.__weight = weight

    def get_info(self):
        return f" овощ: {self._Product__name}, цена: {self._Product__price} рублей, вес: {self.__weight} кг"
    
class Grecory(Product):
    def __init__(self, name, price, quantity):
        super().__init__(name, price)
        self.__quantity = quantity

    def get_info(self):
        return f" продукт: {self._Product__name}, цена: {self._Product__price} рублей, количество: {self.__quantity} шт"
    
class Household(Product):
    def __init__(self, name, price, brand):
        super().__init__(name, price)
        self.__brand = brand

    def get_info(self):
        return f" товар: {self._Product__name}, цена: {self._Product__price} рублей, бренд: {self.__brand}"
    
def main():
    products = []

    for i in range(1, 11):
        products.append(Vegetable(f"редиска {i}", 50 + i * 2))
        
    for i in range(1, 11):
        products.append(Grecory(f"макароны {i}", 80 + i * 5, 1))
        
    for i in range(1, 11):
        products.append(Household(f"шампунь {i}", 150 + i * 10, f"Бренд {i}"))

    for product in products:
        print(product.get_info())

        if hasattr(product, '_Product__price'):
            print(f"Цена: {product._Product__price} рублей")
            
if __name__ == "__main__":    main()
