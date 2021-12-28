from tkinter import *
window=Tk()
window.geometry("400x500")
window.title("Area of triangle")
H=Label(window,text="Area of Triangle",fg="green")
H.place(x=150,y=30)

text=Label(window,text="Height",fg="brown")
text1=Entry(window)
text1.place(x=200,y=90)
text.place(x=100,y=90)

A=Label(window,text="Base",fg="brown")
text2=Entry(window)
text2.place(x=200,y=110)
A.place(x=100,y=110)

def area():
    HEIght=int(text1.get())
    BASe=int(text2.get())
    Area=(HEIght*BASe)/2
    Label(window,text=str(Area),fg="brown").place(x=100,y=180)



B=Button(window,text="calculate",command=area)
B.place(x=100,y=150)

window.mainloop()