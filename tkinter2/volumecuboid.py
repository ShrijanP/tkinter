from tkinter import *
window=Tk()
window.geometry("400x300")
window.title("perform volume of cuboid")

H=Label(window,text="perform volume of cuboid",fg="green")
H.place(x=150,y=30)

text=Label(window,text="length",fg="red")
text1=Entry(window)
text1.place(x=200,y=90)
text.place(x=100,y=90)

A=Label(window,text="Height",fg="red")
A1=Entry(window)
A1.place(x=200,y=120)
A.place(x=100,y=120)

B=Label(window,text="Breadth",fg="red")
B1=Entry(window)
B1.place(x=200,y=150)
B.place(x=100,y=150)

def Volume():
    len=float(text1.get())
    Volume=(len)**3
    Label(window,text=str(Volume),fg="red").place(x=100,y=220)



B=Button(window,text="calculate",command=Volume,fg="red")
B.place(x=100,y=180)

C=Button(window,text="exit",command=lambda:exit(),fg="red")
C.place(x=230,y=180)

window.mainloop()
