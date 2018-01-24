#! /usr/bin/python3.5

import hashlib

valStr="0000000"
maxValKey = 9999999999


def hashValidator(theHash: object, valString: object, valKey: object) -> object:
    if theHash[:len(valString)] == valString:
        print(theHash)
        print(valKey)
        quit()


for valKey in range(0,maxValKey):
    proposal = "this is a test proposal that can be used for contracts" + str(valKey)
    hashValidator(hashlib.sha512(proposal.encode('utf-8')).hexdigest(), valStr, valKey)

print("No hash found")
