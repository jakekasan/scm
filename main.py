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

# sampleTransaction = {
#     "orderRef":1,
#     "inputs":[
#         {
#             "inputRef":12345,
#             ""
#         }
#     ]
# }

# define actors

genesisData = [
    {
        "type":"AUTH",
        "data":{
            "key":"keyOfOrderActor",
            "auth":False
        },
        "byWhom":"keyOfAuthorisor",
        "signature":"signatureOfAuthorisor"
    },
    {
        "type":"AUTH",
        "data":{
            "key":"keyOfWarehouseActor",
            "auth":False
        },
        "byWhom":"keyOfAuthorisor",
        "signature":"signatureOfAuthorisor"
    },
    {
        "type":"AUTH",
        "data":{
            "key":"keyOfShippingActor",
            "auth":False
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
    }
]





def main():

    # print("\nString of dict:\n")
    # print(str(genesisData))

    # print("\nJson loads on string:\n")
    # print(json.loads(json.dumps(genesisData))[0]["type"])

    # print("\nJson dumps of dict:\n")
    # print(json.dumps(genesisData))

    newBlock = Block(json.dumps(genesisData),"",difficulty=1)
    blockchain = BlockChain(1)
    blockchain.addBlock(newBlock)

    print(blockchain)

    return


if __name__ == '__main__':
    main()
