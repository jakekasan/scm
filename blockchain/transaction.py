class Transaction:
    def __init__(self,type):
        self.time = "12:45"
        pass

    def signTransaction(self,privateKey):
        pass

class Action(Transaction):
    def __init__(self,actor=None,inputs=None,subType=None):
        super().__init__("ACTION")
        self.actor = actor
        self.inputs = inputs
        self.subType = None
        pass

    def __str__(self):
        return json.dumps({

        })

class Auth(Transaction):
    def __init__(self,byWhom,actor,action):
        self.byWhom = byWhom
        self.actor = actor
        self.action = action
        pass

class Info(Transaction):
    def __init__(self):
        pass

class Model(Transaction):
    def __init__(self,name,id,requirements):
        self.name = name
        self.id = id
        self.requirements = requirements

