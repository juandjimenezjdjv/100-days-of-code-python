'''mod'''
from tkinter import *

def button_click():
    '''func'''
    print("I got clicked")
    new_txt=input.get()
    my_label.config(text=new_txt)

window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20,pady=20 )

#Label
my_label=Label(text="Im a label", font=("Arial",24,"bold"))
my_label.config(text="New Text")
my_label.grid(column=0, row=0)

#button
button=Button(text="Click Me", command=button_click)
button.grid(column=1, row=1)
boton=Button(text="Here", command=button_click)
boton.grid(column=2, row=0)


#Entry
input=Entry(width=10)
print(input.get())
input.grid(column=3, row=2)






window.mainloop()
