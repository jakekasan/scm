import hashlib

class Block:
    def __init__(self,data,previousHash,currentHash=None,nonce=None,difficulty=1):
        self.data = data
        self.previousHash = previousHash
        self.difficulty = difficulty
        if (currentHash is None) | (nonce is None):
            self.nonce = 0
            self.currentHash = self.mineBlock()
        else:
            self.nonce = nonce
            self.currentHash = currentHash
        pass

    def hashBlock(self):
        to_hash = {
            "data":self.data,
            "previousHash":self.previousHash,
            "date":self.getDate(),
            "nonce":self.nonce
        }
        hash = self.hashThis(to_hash)
        return hash

    def hashThis(self,data):
        if type(data) != str:
            data = str(data)
        h = hashlib.new("sha256")
        h.update(data.encode())
        return h.hexdigest()

    def getDate(self):
        return "January 1st, 2005"

    def __str__(self):
        return "blockHash: {}\nnonce: {}\nprevHash: {}\ndata: {}".format(self.currentHash,self.nonce,self.previousHash,self.data)

    def mineBlock(self):
        blockhash = self.hashBlock()
        while blockhash[:self.difficulty] != ("".join(["0" for _ in range(self.difficulty)])):
            #print("{} : {}".format(blockhash[:self.difficulty],("".join(["0" for _ in range(self.difficulty)]))))
            self.nonce += 1
            blockhash = self.hashBlock()
        return blockhash
        

    def returnBlock(self):
        return {
            "data":self.data,
            "previousHash":self.previousHash,
            "date":self.getDate(),
            "nonce":self.nonce,
            "hash":self.currentHash
        }
