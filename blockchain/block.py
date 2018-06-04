import hashlib

class Block:
    def __init__(self,data,previousHash):
        self.data = data
        self.previousHash = previousHash
        self.nonce = 0
        self.currentHash = self.hashBlock()
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


    def mineBlock(self):
        while self.currentHash[:self.difficulty] != ("".join(["0" for _ in range(self.difficulty)])):
            self.nonce += 1
            self.currentHash = self.hashBlock()

    def returnBlock(self):
        return {
            "data":self.data,
            "previousHash":self.previousHash,
            "date":self.getDate(),
            "nonce":self.nonce,
            "hash":self.currentHash
        }
