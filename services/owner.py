"""

Owner class

"""


class Owner:
    def __init__(self,name,publicKey):
        self.name = name
        self.publicKey = publicKey
        pass

    def sign(self,data):
        # return signature of data
        pass
