"""

This is the pool class, which will serve as a prototype for all the other pools created for individual services.

"""

class Pool:
    def __init__(self,network):
        self.network = network
        self.addr = network.assignAddr(self)
        self.pool = []

    def get(self):
        if len(self.pool) < 1:
            return None
        return random.choice(self.pool)

    def post(self,data):
        self.pool.append(data)
        return None

    def push(self,item):
        self.pool.append(item)

    def __str__(self):
        return "Pool with {} items".format(len(self.pool))
