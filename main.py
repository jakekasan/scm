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
from blockchain.block import Block
from blockchain.blockchain import BlockChain

import json


class Transaction:
    def __init__(self,data):
        pass

    def sign(self,private_key):
        pass

genesisData = [
    {
        "type":"AUTH",
        "data":{
            "key":"keyOfOrderActor",
            "auth":True
        },
        "byWhom":"keyOfAuthorisor",
        "signature":"signatureOfAuthorisor"
    },
    {
        "type":"AUTH",
        "data":{
            "key":"keyOfWarehouseActor",
            "auth":True
        },
        "byWhom":"keyOfAuthorisor",
        "signature":"signatureOfAuthorisor"
    },
    {
        "type":"AUTH",
        "data":{
            "key":"keyOfShippingActor",
            "auth":True
        },
        "byWhom":"keyOfAuthorisor",
        "signature":"signatureOfAuthorisor"
    },
    {
        "type":"ACTION",
        "subType":"createdProduct"
    },
    {
        "type":"ACTION",
        "subType":"locationAtShipping"
    },
    {
        "type":"ACTION",
        "subType":"confirmationOfShipping"
    },
    {
        "type":"MODEL",
        "data":{
            "name":"finishedProduct",
            "inputs":[
                {
                    "type":"ACTION",
                    "subType":"createdProduct"
                },
                {
                    "type":"ACTION",
                    "subType":"locationAtShipping"
                },
                {
                    "type":"ACTION",
                    "subType":"confirmationOfShipping"
                }
            ]
        }
    },
    {
        ""
    }
]




def main():


    newBlock = Block(json.dumps(genesisData),"",difficulty=1)
    blockchain = BlockChain(1)
    blockchain.addBlock(newBlock)

    print(blockchain)

    print("Actors: ")
    print(blockchain.buildActors())

    return


if __name__ == '__main__':
    main()
