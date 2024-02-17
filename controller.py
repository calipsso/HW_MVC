from model import Shoe

class ShoeController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
    def addShoe(self,ids, gender_type, types, color, price, brand, size):
        shoe = Shoe(ids, gender_type, types, color, price, brand, size)
        self.model.addShoe(shoe)

    def showShoes(self):
        store = self.model.showShoe
        self.view.displey_shoe(store)




