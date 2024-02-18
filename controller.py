from model import Shoe


class ShoeController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
    def addShoe(self,ids, gender_type, types, color, price, brand, size):
        shoe = Shoe(ids, gender_type, types, color, price, brand, size)
        self.model.addShoe(shoe)
    def removeShoe(self,id):
        self.model.removeShoe(id)
        self.showShoes()
    def showShoes(self):
        store = self.model.showShoe()
        self.view.showShoe(store)

    def shoeSize(self, sizeOfShoe):
        self.model.shoeSize(sizeOfShoe)
        self.showShoes()
    def totalShoePrice(self):
        self.model.totalShoePrice()
        self.showShoes()






