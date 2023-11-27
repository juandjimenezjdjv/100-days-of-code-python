'''mod'''
from tkinter import *

def button_click():
    '''func'''
    new_txt=input_mile.get()
    new_txt=round(int(new_txt)*1.609)
    result.config(text=new_txt)

window = Tk()
window.title("Mile to Km converter")
window.minsize(width=300, height=200)
window.config(padx=20,pady=20 )

#Label
equal=Label(text="is equal to", font=("Arial",12))
equal.grid(column=0, row=1)
miles=Label(text="Miles", font=("Arial",12))
miles.grid(column=2, row=0)
km=Label(text="Km", font=("Arial",12))
km.grid(column=2, row=1)
result=Label(text=0)
result.grid(column=1, row=1)

#Entry
input_mile=Entry(width=10)
input_mile.grid(column=1, row=0)

button=Button(text="Calculate", command=button_click)
button.grid(column=1, row=2)


window.mainloop()
