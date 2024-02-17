from model import Shoe
from model import ShoeModel
from controller import ShoeController
from view import ShoeView

model = ShoeModel()
view = ShoeView()
controller = ShoeController(model, view)

controller.addShoe(1, "male", "sneakers", "red", 179,"Nike", 41)
controller.addShoe(2, "female", "sneakers", "blue", 149,"Adidas", 40)

controller.showShoes()