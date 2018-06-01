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
        return [x for x in self.addrs.keys()]

    def freeAddrList(self):
        return [x for x in self.addrs.keys() if self.addrs[x] == None]

    def usedAddrList(self):
        return [x for x in self.addrs.keys() if self.addrs[x] != None]

    def addrListString(self):
        return str(self.addrList())

    def assignAddr(self,thing):
        addr = random.choice(self.freeAddrList())
        self.addrs[addr] = thing
        return addr

    def __str__(self):
        resultString = []
        for addr in self.usedAddrList():
            resultString.append("{} : {}\n".format(addr,self.addrs[addr].__str__()))
        return "".join(resultString)
