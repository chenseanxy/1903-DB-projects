import json

class Hotel(object):
    def __init__(self, tup):
        if(type(tup) == tuple):
            self.hotelNum = tup[0]  #str
            self.location = tup[1]  #str
            self.price = tup[2]     #int
            self.numRooms = tup[3]  #int
            self.numAvail = tup[4]  #int
            self.param = json.loads(tup[5])

        if(type(tup) == str):
            d = json.loads(tup)
            self.hotelNum = d["hotelNum"]
            self.location = d["location"]
            self.price = d["price"]
            self.numRooms = d["numRooms"]
            self.numAvail = d["numAvail"]
            self.param = d["param"]


    def toTuple(self):
        return (self.hotelNum,
                self.location,
                self.price,
                self.numRooms,
                self.numAvail,
                json.dumps(self.param))
    
    def toUpdateTuple(self):
        return (self.location,
                self.price,
                self.numRooms,
                self.numAvail,
                json.dumps(self.param),
                self.hotelNum )

    def __str__(self):
        return f"[HOTEL] {self.toTuple()}"

    def isFull(self):
        return self.numAvail <= 0
    
    def occupancy(self):
        return "{:.2f}".format(1-(self.numAvail/self.numRooms))

if __name__ == "__main__":
    param = {"someparam": "something"}
    h = Hotel(("11", "Shenzhen", 12, 48, 48, json.dumps(param)))
    print(h)

