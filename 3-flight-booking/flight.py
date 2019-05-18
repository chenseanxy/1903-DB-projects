import json

class Flight(object):
    def __init__(self, tup):
        if(type(tup) == tuple):
            self.flightNum = tup[0] #str
            self.price = tup[1]     #int
            self.numSeats = tup[2]  #int
            self.numAvail = tup[3]  #int
            self.fromCity = tup[4]  #str
            self.arivCity = tup[5]  #str
            self.param = json.loads(tup[6]) #dict
    
        if(type(tup) == str):
            d = json.loads(tup)
            self.flightNum = d["flightNum"]
            self.fromCity = d["fromCity"]
            self.arivCity = d["arivCity"]
            self.price = d["price"]
            self.numSeats = d["numSeats"]
            self.numAvail = d["numAvail"]
            self.param = d["param"]

    def toTuple(self):
        return (self.flightNum,
                self.price,
                self.numSeats,
                self.numAvail,
                self.fromCity,
                self.arivCity,
                json.dumps(self.param))
        
    def toUpdateTuple(self):
        return (self.price,
                self.numSeats,
                self.numAvail,
                self.fromCity,
                self.arivCity,
                json.dumps(self.param),
                self.flightNum)

    def __str__(self):
        return f"[FLIGHT] {self.toTuple()}"
    
    def isFull(self):
        return self.numAvail <= 0
    
    def occupancy(self):
        return "{:.2f}%".format(1-(self.numAvail/self.numSeats))


if __name__ == "__main__":
    param = {"takeoff": 12800}
    f = Flight(("11", 12, 48, 48, "SZX", "LAX",json.dumps(param)))
    print(f)