import json

class Customer(object):
    def __init__(self, tup):
        if(type(tup) == tuple):
            self.custID = tup[0]    #int
            self.custName = tup[1]  #str
        
        if(type(tup) == str):
            cust = json.loads(tup)
            self.custID = cust["custID"]
            self.custName = cust["custName"]
    
    def toTuple(self):
        return (self.custID, \
                self.custName)
    
    def toUpdateTuple(self):
        return (self.custName, \
                self.custID)

    def __str__(self):
        return f"[CUSTOMER] {self.toTuple()}"
