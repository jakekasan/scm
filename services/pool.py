"""
Pool class

"""

class Pool:
    def __init__(self):
        self.items = []

    def get(self):
        return

    def submit(self,order):
        order = self.validateOrder(order)
        if order != None:
            self.pool.append(order)
            return True
        else:
            return False

    def validateOrder(self,order):
        return order
