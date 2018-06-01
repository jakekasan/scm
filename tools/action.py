"""
This object will be passed around and processed by the services
"""

import datetime

class Action:
    def __init__(self,name,description):
        self.name = name
        self.description = description
        self.time = datetime.datetime.now()

    def __str__(self):
        return "\t{} : {}\n".format(self.name,self.description)
