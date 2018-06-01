class Resource:
    def __init__(self,name,desc,id):
        self.name = name
        self.desc = desc
        self.id = id

    def __str__(self):
        return "{} : {} : {}".format(self.id,self.name,self.desc)
