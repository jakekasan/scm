import datetime as datetime

class Product:
    def __init__(self,name):
        self.name = name
        self.dateCreated = datetime.datetime.now()

    def getObject(self):
