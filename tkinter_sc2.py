from tkinter import *

window=Tk()

def my_converter():
	kg=float(value.get())
	gram=kg*1000
	pou=kg*2.20462
	oun=kg*35.274
	t1.insert(END,gram)
	t2.insert(END,pou)
	t3.insert(END,oun)

b1=Button(window,text="convert",command=my_converter)
b1.grid(row=0,column=3)

value=StringVar()
e1=Entry(window,textvariable=value)
e1.grid(row=0,column=2)

l=Label(window,text="kg")
l.grid(row=0,column=0)
t1=Text(window,height=1,width=20)
t1.grid(row=1,column=0)
t2=Text(window,height=1,width=20)
t2.grid(row=1,column=1)
t3=Text(window,height=1,width=20)
t3.grid(row=1,column=2)
window.mainloop()