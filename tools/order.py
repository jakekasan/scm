class Order:
    def __init__(self):
        self.id = self.generateID()
        self.date = datetime.datetime.now()
        self.inputs = []

    def generateID(self):
        return "01234"

    def validateOrder(self):
        """
        Check inputs
        """
        pass
