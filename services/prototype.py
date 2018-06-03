"""

The prototype service class from which all the other classes will inherit methods and properties

"""

class Prototype:
    def __init__(self):
        self.inputPool = None
        self.outputPool = None

    def submitToOutputPool(self,order):
        result = self.outputPool.submit(order)
        if (result):
            return True
        return False

    def getFromInputPool(self):
        order = self.inputPool.get()
        if (order == False):
            return None
        return order

    def processOrder(self):
        
