"""

This is the pool class, which will serve as a prototype for all the other pools created for individual services.

"""

class Pool:
    def __init__(self,addr):
        self.addr = addr
        self.pool = []
        pass

    def push(self,item):
        self.pool.append(item)
