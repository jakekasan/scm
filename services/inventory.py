"""
This is where orders will pass to from billing where they will be associated with a valid product. The product must contain valid
raw material inputs as well as a location input that proves they are located in the inventory. Once these requirements are fulfilled,
the order will be moved to shipping.


The class

init():

Each instance of the class will be associated with the addresses of the manufacturing and shipping pools. Also any other information about the
inventory will be associated here, such as location, list of other nodes it is aware of.


"""



class Inventory:
    def __init__(self):
        pass

    def parseOrder(self):
        pass

    def finishProcessing(self):
        pass
