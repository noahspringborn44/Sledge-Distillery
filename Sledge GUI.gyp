import tkinter as tk # Import tkinter
from tkinter import *
import tkinter.font

window = Tk()
qdict = {'1 Large Bottle':2,
'2 Large Bottles':4,
'1 Large Bottle - 1 Small Bottle':3,
'1 Large Bottle - 2 Small Bottles':4,
'1 Small Bottle':1,
'2 Small Bottles':2,
'3 Small Bottles':3,
'4 Small Bottles':4
}

#After the GO button is selected this function runs which checks the DB and checks if the customer reached their limit. 
#It then runs the appropriate function based off the answer
def quantitycheck():

    amount = qdict[quantity.get(ACTIVE)]
    print(amount)
    #When we connect to database
    #customer_total = cursor.execute(SELECT SUM Amount FROM CustomerOrders WHERE ID = id)
    if customer_total + amount < 5:
        #Function to allow the purchase to go through
        #Also needs to open the new window with green accept button
        print()
    else:
        #Function that says deny
        print()


#Creating the main view for the first order screen

window['bg'] = 'white'
window.title("Sledge Distillery Purchase Tracker")

#Adding the logo to the top
photo = PhotoImage(file="/Users/austi/OneDrive/Desktop/Sledge Distillery Logo.png")  
photo = photo.zoom(9,6) 
photo = photo.subsample(50,40)
Label(window, image = photo, background='white',).grid(row = 1, column = 3,sticky='')

#adding a title next to the logo
Label(window, text = 'Sledge ID Verification', background = 'white', justify = 'left', font = ('Times', 24, 'bold')).grid(row = 1, column = 1, columnspan = 2, sticky = '')

#DL ID input
Label(window, text = "Driver's License ID:", background='white', height = 2, font = 12).grid(row = 2, column = 1,columnspan = 1, sticky='') 
id = StringVar()
Entry(window, textvariable = id, justify = LEFT, background='white', width = 24).grid(row=2, column=2,columnspan = 2, sticky='')

#Quantity Drop Down and Input
Label(window, text = "Quantity:", background='white', height = 2, font = 12).grid(row = 4, column = 1,columnspan = 1,sticky='')

#Adding the different quantities of bottles to the Drop Down Box
clicked = StringVar()
quantity = OptionMenu(window, clicked, '1 Large Bottle', '2 Large Bottles', '1 Large Bottle - 1 Small Bottle',
'1 Large Bottle - 2 Small Bottles', '1 Small Bottle', '2 Small Bottles', '3 Small Bottles', '4 Small Bottles')
quantity.grid(row = 4, column = 2,columnspan = 2)


#use command to run a function when the button is selected
#also can look into using activebackground and activeforeground
##Label(window, text = "", background='white').grid(row = 5, column = 1)

goButton = Button(window,bg = 'white',text = ' GO ', font = ('Arial', 16, 'bold'), command = quantitycheck).grid(row = 6, column = 2)

#Determining the whole window size and also starts the loop            
window.grid_columnconfigure(3,minsize=200)
window.grid_rowconfigure(6,minsize=200)   
window.mainloop()

