import json

class Reservation(object):
    def __init__(self, tup):
        if(type(tup) == tuple):
            self.resvNum = tup[0]   #str
            self.custID = tup[1]    #int
            self.resvType = tup[2]  #int
            self.resvKey = tup[3]   #str
        
        if(type(tup) == str):
            res = json.loads(tup)
            self.resvNum = res["resvNum"]
            self.custID = res["custID"]
            self.resvType = res["resvType"]
            self.resvKey = res["resvKey"]
    
    def toTuple(self):
        return (self.resvNum,
                self.custID,
                self.resvType,
                self.resvKey)
    
    def toUpdateTuple(self):
        return (self.custID,
                self.resvType,
                self.resvKey,
                self.resvNum)

    def __str__(self):
        return f"[RESERVATION] {self.toTuple()}"