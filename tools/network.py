"""

This class creates a fake network and handles communications between nodes. Its better than starting a real HTTP server for each service...

"""

import random as random


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

    def addrList(self):
        return [x for x in self.addrs.keys() if x not None]

    def addrListString(self):
        return str(addrList())

    def assignAddr(self,thing):
        addr = random.choice(addrList())
        self.addrs[addr] = thing
        return addr

    def __str__(self):
        resultString = []
        for addr in addrList():
            resultString.append("{} : {}".format(addr,self.addrs[addr].__str__()))
