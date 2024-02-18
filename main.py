from model import Shoe
from model import ShoeModel
from controller import ShoeController
from view import ShoeView

model = ShoeModel()
view = ShoeView()
controller = ShoeController(model, view)

controller.addShoe(1, "male", "sneakers", "red", 179,"Nike", 41)
controller.addShoe(2, "female", "sneakers", "blue", 149,"Adidas", 40)
controller.addShoe(3, "female", "moonboots", "silver", 949,"Dior", 40)
controller.addShoe(4, "female", "track", "pinkBlue", 99,"Vans", 39)
controller.addShoe(5, "male", "track", "pink", 199,"Ck", 42)
controller.addShoe(6, "male", "sneakers", "black", 71,"ECCO", 39)
print("---------- 1")
controller.showShoes()
print("---------- 2")
controller.removeShoe(1)
print("---------- 3")
controller.shoeSize(39)
print("---------- 4")
controller.totalShoePrice()
