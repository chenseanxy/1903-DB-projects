import json


class Flight(object):
    def __init__(self, tup):
        if(type(tup) == tuple):
            self.flightNum = tup[0]  # str
            self.price = tup[1]  # int
            self.numSeats = tup[2]  # int
            self.numAvail = tup[3]  # int
            self.fromCity = tup[4]  # str
            self.arivCity = tup[5]  # str
            self.param = json.loads(tup[6])  # dict

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


class Hotel(object):
    def __init__(self, tup):
        if(type(tup) == tuple):
            self.hotelNum = tup[0]  # str
            self.location = tup[1]  # str
            self.price = tup[2]  # int
            self.numRooms = tup[3]  # int
            self.numAvail = tup[4]  # int
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
                self.hotelNum)

    def __str__(self):
        return f"[HOTEL] {self.toTuple()}"

    def isFull(self):
        return self.numAvail <= 0

    def occupancy(self):
        return "{:.2f}".format(1-(self.numAvail/self.numRooms))


class Bus(object):
    def __init__(self, tup):
        if(type(tup) == tuple):
            self.busNum = tup[0]  # str
            self.location = tup[1]  # str
            self.price = tup[2]  # int
            self.numSeats = tup[3]  # int
            self.numAvail = tup[4]  # int
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


class Customer(object):
    def __init__(self, tup):
        if(type(tup) == tuple):
            self.custID = tup[0]  # int
            self.custName = tup[1]  # str

        if(type(tup) == str):
            cust = json.loads(tup)
            self.custID = cust["custID"]
            self.custName = cust["custName"]

    def toTuple(self):
        return (self.custID,
                self.custName)

    def toUpdateTuple(self):
        return (self.custName,
                self.custID)

    def __str__(self):
        return f"[CUSTOMER] {self.toTuple()}"


class Reservation(object):
    def __init__(self, tup):
        if(type(tup) == tuple):
            self.resvNum = tup[0]  # str
            self.custID = tup[1]  # int
            self.resvType = tup[2]  # int
            self.resvKey = tup[3]  # str

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
