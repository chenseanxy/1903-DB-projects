from mysql_db import *
from entities import *

def getTable(obj):
    if(type(obj) == Flight):
        return "flights"
    if(type(obj) == Hotel):
        return "hotels"
    if(type(obj) == Bus):
        return "bus"

def getKeyName(table):
    if(table == "flights"):
        keyName = "flightNum"
    if(table == "hotels"):
        keyName = "hotelNum"
    if(table == "bus"):
        keyName = "busNum"
    if(table == "reservations"):
        keyName = "resvNum"
    if(table == "customers"):
        keyName = "custID"
    return keyName

def add(obj):
    print(f"[BACKEND] Adding {obj}") 
    if(type(obj) == Flight):
        query = "INSERT INTO flights VALUES (%s,%s,%s,%s,%s,%s,%s)"
        params = obj.toTuple()
    elif(type(obj) == Hotel):
        query = "INSERT INTO hotels VALUES (%s,%s,%s,%s,%s,%s)"
        params = obj.toTuple()
    elif(type(obj) == Bus):
        query = "INSERT INTO bus VALUES (%s,%s,%s,%s,%s,%s)"
        params = obj.toTuple()
    elif(type(obj) == Customer):
        query = "INSERT INTO customers VALUES (%s,%s)"
        params = obj.toTuple()
    elif(type(obj) == Reservation):
        query = "INSERT INTO reservations VALUES (%s,%s,%s,%s)"
        params = obj.toTuple()
    else:
        print(f"[BACKEND] {obj} is not of valid type!")

    DBConnect.cursor.execute(query, params)
    DBConnect.cnx.commit()

def remove(primaryKey, table):
    item = getValue(primaryKey, table)
    if(item == None):
        return
    query = "DELETE FROM {} WHERE {}=%s".format(table, getKeyName(table))
    print("DELETE FROM {} WHERE {}={}".format(table, getKeyName(table), primaryKey))
    DBConnect.cursor.execute(query, (primaryKey,))
    DBConnect.cnx.commit()

def update(obj):
    print(f"[BACKEND] Updating {obj}") 
    if(type(obj) == Flight):
        query = (f"UPDATE {getTable(obj)} "
                  "SET price=%s, numSeats=%s, numAvail=%s, fromCity=%s, arivCity=%s, param=%s "
                  "WHERE flightNum=%s")
        params = obj.toUpdateTuple()

    elif(type(obj) == Hotel):
        query = (f"UPDATE {getTable(obj)} "
                  "SET location=%s, price=%s, numRooms=%s, numAvail=%s, param=%s "
                  "WHERE hotelNum=%s")
        params = obj.toUpdateTuple()
        
    elif(type(obj) == Bus):
        query = (f"UPDATE {getTable(obj)} "
                  "SET location=%s, price=%s, numSeats=%s, numAvail=%s, param=%s "
                  "WHERE busNum=%s")
        params = obj.toUpdateTuple()
    
    else:
        print(f"[BACKEND] {obj} cannot be updated!")
    
    DBConnect.cursor.execute(query, params)
    DBConnect.cnx.commit()

def getValue(primaryKey, table):
    keyName = getKeyName(table) #Get the PrimaryKey Name from Table Name
    query = f"SELECT * FROM {table} WHERE {keyName}=%s"
    
    DBConnect.cursor.execute(query, (primaryKey,))
    result = DBConnect.cursor.fetchone()

    return createObj(result, table)

def createObj(queryResult, table):
    if(table == "flights"):
        return Flight(queryResult)
    if(table == "hotels"):
        return Hotel(queryResult)
    if(table == "bus"):
        return Bus(queryResult)
    if(table == "reservations"):
        return Reservation(queryResult)
    if(table == "customers"):
        return Customer(queryResult)
    return None

def queryTable(table):
    query = f"SELECT * FROM {table}"
    DBConnect.cursor.execute(query)
    results = DBConnect.cursor.fetchall()
    print(results)

    objects = []

    if(table == "flights"):
        for line in results:
            objects.append(Flight(line))
    if(table == "hotels"):
        for line in results:
            objects.append(Hotel(line))
    if(table == "bus"):
        for line in results:
            objects.append(Bus(line))
    if(table == "reservations"):
        for line in results:
            objects.append(Reservation(line))
    if(table == "customers"):
        for line in results:
            objects.append(Customer(line))
    
    return objects

def newReservation(reservation):
    if(reservation.resvType == 1):  #Flight
        obj = getValue(reservation.resvKey, "flights")

    if(reservation.resvType == 2):  #Hotel
        obj = getValue(reservation.resvKey, "hotels")

    if(reservation.resvType == 3):  #Bus
        obj = getValue(reservation.resvKey, "bus")
    
    if(getValue(reservation.resvNum, "reservations") != None):
        print(getValue(reservation.resvNum, "reservations"))
        print("This reservation number is already taken")
        return
    
    if(getValue(reservation.custID, "customers") == None):
        print("Customer Number does not exist")

    if(obj.isFull() == False):
        obj.numAvail -= 1
        update(obj)
        add(reservation)
    else:
        print(str(obj)+" is not available")
    
def cancelReservation(resvNum):
    reservation = getValue(resvNum, "reservations")
    if(reservation == None):
        print("Reservation is not available")
        return

    if(reservation.resvType == 1):  #Flight
        obj = getValue(reservation.resvKey, "flights")
    if(reservation.resvType == 2):  #Hotel
        obj = getValue(reservation.resvKey, "hotels")
    if(reservation.resvType == 3):  #Bus
        obj = getValue(reservation.resvKey, "bus")
    
    if(obj == None):
        print("Requested item is not available")
        print("Auto-cancelling reservation")
    
    obj.numAvail += 1
    update(obj)
    remove(resvNum, "reservations")

def queryReservation(custID):
    query = "SELECT * FROM reservations WHERE custID=%s"
    DBConnect.cursor.execute(query, (custID,))
    results = DBConnect.cursor.fetchall()

    if(results == None):
        print("Reservations does not exist")
        return None

    objects = []
    for result in results:
        objects.append(Reservation(result))
    return objects
