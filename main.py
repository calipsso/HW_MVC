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
controller.addShoe(4, "female", "track", "PinkBlue", 99,"Dior", 39)
print("---------- 1")
controller.showShoes()
print("---------- 2")
controller.removeShoe(2)