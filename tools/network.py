"""

This class creates a fake network and handles communications between nodes. Its better than starting a real HTTP server for each service...

"""


class Network:
    def __init__(self):
        self.addrs = { x:None for x in range(155) }

    def getRequest(self,addr):
        if self.addrs[addr] == None:
            return "Request failed : no such address"
        else:
            return self.addrs[addr].get()

    def postRequest(self,addr,data):
        if self.addrs[addr] == None:
            return "Request failed : no such address"
        else:
            return self.addrs[addr].post(data)
