class MenuItem:
    
    def __init__(self,name,price,is_available):
        self.name = name
        self.price = price
        self.is_available = is_available

    def describe(self):
        print(self.price)

    def sell(self):
        if not self.is_available:
            print("Sorry, out of stock")

if __name__ == "__main__":
    cafe = MenuItem("Matcha",7, False)
    cafe.describe()
    cafe.sell()
