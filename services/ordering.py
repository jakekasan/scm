"""

This is where orders are first generated. Here a payment action will be prompted, and either an invoice or reciept of payment will be associated with the order

"""

class Ordering:
    def __init__(self):
        pass

    def generateNewOrder(self):
        # return a new order

class Order:
    def __init__(self,products):
        self.products = []


class Product:
    def __init__(self,name,price,requirements):
        self.name = name
        self.price = price
        self.requirements = requirements
        self.fulfilled = []
        self.completed = False

    def addAction(self,action):
        if action in self.requirements:
            self.fulfilled.append(action)
        else:
            print("Error: action not in product blueprint")
        return

    def update(self):
        pass
