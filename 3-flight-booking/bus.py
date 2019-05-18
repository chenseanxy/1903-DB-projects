import json

class Bus(object):
    def __init__(self, tup):
        if(type(tup) == tuple):
            self.busNum = tup[0]    #str
            self.location = tup[1]  #str
            self.price = tup[2]     #int
            self.numSeats = tup[3]  #int
            self.numAvail = tup[4]  #int
            self.param = json.loads(tup[5])

        if(type(tup) == str):
            d = json.loads(tup)
            self.busNum = d["busNum"]
            self.location = d["location"]
            self.price = d["price"]
            self.numSeats = d["numSeats"]
            self.numAvail = d["numAvail"]
            self.param = d["param"]


    def toTuple(self):
        return (self.busNum,
                self.location,
                self.price,
                self.numSeats,
                self.numAvail,
                json.dumps(self.param))

    def toUpdateTuple(self):
        return (self.location,
                self.price,
                self.numSeats,
                self.numAvail,
                json.dumps(self.param),
                self.busNum)

    def __str__(self):
        return f"[BUS] {self.toTuple()}"

    def isFull(self):
        return self.numAvail <= 0
    
    def occupancy(self):
        return "{:.2f}".format(1-(self.numAvail/self.numSeats))

if __name__ == "__main__":
    param = {"someparam": "something"}
    b = Bus(("11", "Shenzhen", 12, 48, 48, json.dumps(param)))
    print(b)

