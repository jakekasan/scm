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
import random
import hashlib
from datetime import datetime


genesisData = [
    {
        "type":"AUTH",
        "data":{
            "key":"keyOfOrderActor",
            "auth":True,
            "ACTIONs":[
                "createdOrder"
            ]
        },
        "byWhom":"keyOfAuthorisor",
        "signature":"signatureOfAuthorisor"
    },
    {
        "type":"AUTH",
        "data":{
            "key":"keyOfWarehouseActor",
            "auth":True,
            "ACTIONs":[
                "createdProduct",
                "locationAtShipping"
            ]
        },
        "byWhom":"keyOfAuthorisor",
        "signature":"signatureOfAuthorisor"
    },
    {
        "type":"AUTH",
        "data":{
            "key":"keyOfShippingActor",
            "auth":True,
            "ACTIONs":[
                "confirmationOfShipping"
            ]
        },
        "byWhom":"keyOfAuthorisor",
        "signature":"signatureOfAuthorisor"
    },
    {
        "type":"ACTION",
        "subType":"createdProduct",
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
        "type":"ACTION",
        "subType":"newOrder"
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


def generateOrders(num):
    orders = []
    for i in range(num):
        newOrder = {
            "type":"REQUEST",
            "orderID":i,
            "items":[
                "finishedProduct",
                "finishedProduct"
            ]
        }
        orders.append(newOrder)
    return orders


def main():
    # genesis block
    newBlock = Block(json.dumps(genesisData),"",difficulty=1)
    blockchain = BlockChain(1)
    blockchain.addBlock(newBlock)

    print(blockchain)


    #known actors
    print("Actors: ")
    print(blockchain.buildActors())

    # let's 'make' a few products to have in storage

    newProducts = []
    for i in range(20):
        productObject = {
            "type":"OBJECT",
            "id":(100+i),
            "name":"finishedProduct",
            "inputs":[
                {
                    "number":0,
                    "type":"ACTION",
                    "subType":"createdProduct",
                    "byWhom":"keyOfWareHouseActor",
                    "date":str(datetime.now()),
                    "signature":signThis({
                        "type":"ACTION",
                        "subType":"createdProduct",
                        "byWhom":"keyOfWarehouseActor",
                        "date":str(datetime.now())
                    },"keyOfWarehouseActor")
                }
            ]
        }
        newProducts.append(productObject)

    productsBlock = Block(json.dumps(newProducts),blockchain.getLastHash())
    blockchain.addBlock(productsBlock)

    # now a few orders will be submitted

    orders = generateOrders(5)

    print("\n")
    print(blockchain)

    ordersBlock = Block(json.dumps(orders),blockchain.getLastHash())
    blockchain.addBlock(ordersBlock)

    print(blockchain)

    print("\n\nNow getting orders...")

    printList(blockchain.buildOrders())

    # now add the shipping action to a few of the orders

    shipping = []
    for _ in range(5):
        temp_action = {
            "type":"ACTION",
            "subType":"locationAtShipping",
            "itemID":getAnOrder(blockchain)[""],
            "byWhom":"keyOfWarehouseActor",
            "date":str(datetime.now()),
            "signature":signThis({
                "type":"ACTION",
                "subType":"locationAtShipping",
                "itemID":getAnOrder(blockchain),
                "byWhom":"keyOfWarehouseActor",
                "date":str(datetime.now())
            })
        }
        shipping.append(temp_action)
    
    shippingBlock = Block(json.dumps(temp_action),blockchain.getLastHash())

    blockchain.addBlock(shippingBlock)

    print(blockchain)
        
    return

def getAnOrder(blockchain):
    orders = blockchain.buildOrders()
    return orders[0]

def printList(arr):
    for x in arr:
        print(x)

def signThis(obj,privateKey):
    h = hashlib.new("sha256")
    h.update((json.dumps(obj)).encode())
    return h.hexdigest()

if __name__ == '__main__':
    main()
