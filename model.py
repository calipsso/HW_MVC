class Shoe:
    def __init__(self, ids, gender_type, types, color, price, brand, size):
        self.ids = ids
        self.gender_type = gender_type
        self.types = types
        self.color = color
        self.price = price
        self.brand = brand
        self.size = size
    def __str__(self):
        return (f"{self.ids}, {self.gender_type}, {self.types}, {self.color}, {self.price}, {self.brand}, {self.size}")
class ShoeModel:
    def __init__(self):
        self.store = []
    def addShoe(self, shoe):
        self.store.append(shoe)
    def removeShoe(self, id):
        self.store = list(filter(lambda shoe: shoe.ids != id, self.store))
        return self.store
    def showShoe(self):
        return self.store
    def shoeSize(self, sizeOfshoe):
        self.store = list(filter(lambda shoe: shoe.size == sizeOfshoe, self.store))
        return self.store
    def totalShoePrice(self):
        totaPrice = 0
        for shoe in self.store:
            totalPrice = totalPrice + shoe["price"]
            return totaPrice







