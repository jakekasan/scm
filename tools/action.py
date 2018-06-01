"""
This object will be passed around and processed by the services
"""

class Action:
    def __init__(self,name,description):
        self.name = name
        self.description = description

    def __str__(self):
        return "\t{} : {}\n".format(self.name,self.description)
