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
    def showShoe(self):
        return self.store
    #def sizeShoe(self, numberOfshoe):
        #for shoe in self.store:
            #if shoe.size == numberOfshoe:
                #return shoe
    #def totalShoePrice(self):
        #totalPrice = 0
        #for shoe in self.store:
            #totalPrice += self.price
        #return totalPrice




