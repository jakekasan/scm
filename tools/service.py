"""

Prototype service class. All services will be based on this class

"""


class Service:
    def __init__(self,network,addr,reqPoolAddr,resPoolAddr):
        self.network = network
        self.addr = self.network.assignAddr()
        self.reqPoolAddr = reqPoolAddr
        self.resPoolAddr = resPoolAddr


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
        """
        Print update about the service
        """
        pass

    def __str__(self):
        return "Service with Req Addr: {} and Res Addr: {}".format(self.reqPoolAddr,self.resPoolAddr)
