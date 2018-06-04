#!/usr/bin/env python3

import os
from Crypto.PublicKey import RSA
from Crypto import Random

def main():
    counter = 0

    # see if theres any other PEM files about

    dir = os.listdir('./')

    for thing in dir:
        if ".pem" in thing or ".PEM" in thing:
            counter += 1

    for _ in range(10):
        rng = Random.new().read
        RSAkey = RSA.generate(1024,rng)
        data = RSAkey.exportKey().decode()
        with open("rsa_{}.pem".format(counter+1),'w') as file:
            file.write(data)
        counter += 1




if __name__ == '__main__':
    main()
