import model
from model import ShoeModel

class ShoeView:
    def showShoe(self, store):
        for shoe in store:
            print(f"{store}")
