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

    def checkAction(self,action):


    def update(self):
        pass

class Action:
    def __init__(self,inputs,type,outputs):
        self.inputs = inputs
        self.type = type
        self.outputs = outputs
        self.signature = self.signAction(owner)

    def signAction(self,owner):
        return "signature"

class Input:
    def __init__(self,owner,id):
        self.owner = owner
        self.id = id
