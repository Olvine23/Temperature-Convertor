import tkinter 
from tkinter import *
#these are the global variables
temp_c = None
temo_f = None

#function called when button  is pressed
def convert():
    global temp_c
    global temp_f
    #converts the celsius to Farenheit and update the label (through textVariable)

    try:
        val = temp_c.get()
        temp_f.set((val * 9.0 /5)+32)
    except:
        pass
root = Tk()
root.title("Temperature Converter")
frame = Frame(root)
frame.pack(fill = BOTH , expand = True)

 
temp_c = DoubleVar()
temp_f = DoubleVar()

entry_celsius = Entry(frame, width = 7 , textvariable = temp_c)
label_unitc = Label(frame, text = "C ")
label_equal = Label(frame , text = "is equal to ")
label_fareheit = Label(frame, textvariable  = temp_f, fg="red")
label_unitf = Label(frame, text = "F")
button_convert = Button(frame, text = "Convert", command = convert , bg = "lightblue")

entry_celsius.grid(row =0, column = 1, padx = 5, pady = 5)
label_unitc.grid(row = 0 , column = 2, padx = 5, pady= 5, sticky = W)
label_equal.grid(row = 1, column =0 , padx =5 , pady = 5 , sticky=E)
label_fareheit.grid(row = 1, column =1 , padx = 5, pady = 5)
label_unitf.grid(row = 1, column  =2, padx = 5, pady =5, sticky = W)
button_convert.grid(row = 2, column = 1, columnspan = 2, padx =5, pady = 5 ,sticky = E)
entry_celsius.focus()
root.mainloop()