"""

Prototype service class. All services will be based on this class

"""


class Service:
    def __init__(self,network,reqPoolAddr,resPoolAddr):
        self.network = network
        self.addr = self.network.assignAddr(self)
        self.reqPoolAddr = reqPoolAddr
        self.resPoolAddr = resPoolAddr
        self.working = False

    def get(self):
        """
        GET request handling
        """
        return "Service at {} replying to GET request".format(self.addr)

    def post(self,data):
        """
        POST request handling
        """
        return "Service at {} replying to POST request".format(self.addr)

    def fetchRequest(self):
        return self.network.getRequest(self.reqPoolAddr)

    def update(self):
        if not self.working:
            self.network.getRequest(self.reqPoolAddr)
        pass

    def __str__(self):
        return "Service with Req Addr: {} and Res Addr: {}".format(self.reqPoolAddr,self.resPoolAddr)
