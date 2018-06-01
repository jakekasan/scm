#!/usr/bin/env python3

"""

Imports:

    tools
        network
        pool
        service

"""

from tools.network import Network
from tools.pool import Pool
from tools.service import Service


def main():

    theNetwork = Network()
    reqPool = Pool(theNetwork)
    resPool = Pool(theNetwork)
    theService = Service(theNetwork,resPool.addr,reqPool.addr)

    print(theNetwork)

    """

    The core while loop

    """
    # while(True):
    #     # Do some stuff...
    #
    # pass

    return


if __name__ == '__main__':
    main()
