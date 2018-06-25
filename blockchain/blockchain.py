class BlockChain:
    def __init__(self,genesisBlock=None,blockchain=None):
        self.blocks = []
        
    
    def validateBlocks(self):
        """
        validate all blocks in the chain
        """
        pass

    def buildActors(self):
        """
        get a list of authorised actors from blocks
        """
        pass

    def buildOrders(self):
        """
        get list of orders (both outstanding and fullfilled)
        """
        pass

    def buildMasters(self):
        """
        set masters from genesis block
        """
        pass

    