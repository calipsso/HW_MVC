from model import Shoe
from model import ShoeModel
from controller import ShoeController
from view import ShoeView

model = ShoeModel()
view = ShoeView()
controller = ShoeController(model, view)

controller.addShoe(1, "male", "sneakers", "red", 179,"Nike", 41)
controller.showShoes()