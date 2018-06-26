import json

class BlockChain:
    def __init__(self,difficulty=1,genesisBlock=None,blockchain=None):
        self.blocks = []
        self.difficulty = difficulty

    def addBlock(self,block):
        self.blocks.append(block)
        
    
    def validateBlocks(self):
        """
        validate all blocks in the chain
        """
        pass

    def buildActors(self):
        actors = []
        for block in self.blocks:
            for transaction in json.loads(block.data):
                if transaction["type"] == "AUTH":
                    if transaction["data"]["auth"] == True:
                        actors.append(transaction["data"]["key"])
        return actors

    def buildOrders(self):
        orders = []
        for block in self.blocks:
            for transaction in block.data:
                orders.append("blah")
        """
        get list of orders (both outstanding and fullfilled)
        """
        pass

    def buildMasters(self):
        pass

    def __str__(self):
        return "".join(["{}\n".format(x.__str__()) for x in self.blocks])

    