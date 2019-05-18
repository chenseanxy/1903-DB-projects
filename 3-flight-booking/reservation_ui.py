from tkinter import *
import backend
from reservation import Reservation

class ReservationUI(object):
    def __init__(self):

        self.tk = Tk()
        tk.title("Reservation UI")

        self.ops = ["Add New Reservation", "Cancel Existing Reservation"]
        self.op = StringVar(self.tk)
        self.op.set(self.ops[0])
        self.opOption = OptionMenu(self.tk, self.op, *self.ops, command = self.updateFrame)
        self.opOption.configure(pady=5)
        self.opOption.grid(row=0, column=0)

        self.createFrame()

        self.tk.mainloop()

    def createFrame(self):
        op = self.op.get()

        self.modifyFrame = Frame(self.tk)
        self.modifyFrame.grid(row=2, column=0, columnspan=2, padx=20, pady=20) 

        self.resvNumText = Label(self.modifyFrame, text="Reservation Number", anchor="e", width=20)
        self.resvNumText.grid(row=0, column=0)
        self.resvNum = Entry(self.modifyFrame, width=40)
        self.resvNum.grid(row=0, column=1)

        self.custIDText = Label(self.modifyFrame, text="Customer ID", anchor="e", width=20)
        self.custIDText.grid(row=1, column=0)

        self.resvTypeText = Label(self.modifyFrame, text="Reservation Type", anchor="e", width=20)
        self.resvTypeText.grid(row=2, column=0)

        self.resvKeyText = Label(self.modifyFrame, text="Reservation Key", anchor="e", width=20)
        self.resvKeyText.grid(row=3, column=0)

        if(op=="Add New Reservation"):
            self.custID = Entry(self.modifyFrame, width=40)
            self.custID.grid(row=1, column=1)

            self.resvType = Entry(self.modifyFrame, width=40)
            self.resvType.grid(row=2, column=1)

            self.resvKey = Entry(self.modifyFrame, width=40)
            self.resvKey.grid(row=3, column=1)
            
            self.commitButton = Button(self.modifyFrame, text="Confirm", pady=5, width=20, command=self.commitChanges)
            self.commitButton.grid(columnspan=2, pady=10)


        if(op=="Cancel Existing Reservation"):
            self.custIDValue = Label(self.modifyFrame, text="", anchor="e", width=20)
            self.custIDValue.grid(row=1, column=1)

            self.resvTypeValue = Label(self.modifyFrame, text="", anchor="e", width=20)
            self.resvTypeValue.grid(row=2, column=1)

            self.resvKeyValue = Label(self.modifyFrame, text="", anchor="e", width=20)
            self.resvKeyValue.grid(row=3, column=1)

            self.fillValuesButton = Button(self.modifyFrame, text="Check", command=self.fillValues)
            self.fillValuesButton.grid(row=0, column=2)

            self.cancelReservationButton = Button(self.modifyFrame, text="Cancel Reservation", pady=5, width=20, command=self.cancelReservation)
            self.cancelReservationButton.grid(columnspan=2, pady=10)


    def updateFrame(self, *args):
        self.modifyFrame.destroy()
        self.createFrame()
    
    def commitChanges(self, *args):
        # Add reservation, on click "Confirm"
        reservation = Reservation((
            self.resvNum.get(),
            int(self.custID.get()),
            int(self.resvType.get()),
            self.resvKey.get()
        ))
        backend.newReservation(reservation)

    def cancelReservation(self):
        backend.cancelReservation(self.resvNum.get())
        

    def fillValues(self, *args):
        resvNum = self.resvNum.get()
        print(f"[UI] Fill Reservation Values on {resvNum}")
        obj = backend.getValue(resvNum, "reservations")
        
        self.fromCity.delete(0, last="end")
        self.fromCity.insert(0, obj.fromCity)
        self.arivCity.delete(0, last="end")
        self.arivCity.insert(0, obj.arivCity)
        self.price.delete(0, last="end")
        self.price.insert(0, obj.price)
        self.totalNum.delete(0, last="end")
        self.totalNum.insert(0, obj.numSeats)
        self.availNum.delete(0, last="end")
        self.availNum.insert(0, obj.numAvail)
        
        self.param.delete(0, last="end")
        self.param.insert(0, obj.param)

if __name__ == "__main__":
    ReservationUI()

