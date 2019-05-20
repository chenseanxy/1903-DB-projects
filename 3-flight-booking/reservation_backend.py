from backend import *

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