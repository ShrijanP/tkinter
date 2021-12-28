from tkinter import *
window=Tk()
window.geometry("400x300")
window.title("Area of circle")

H=Label(window,text="Area of circle",fg="blue")
H.place(x=150,y=30)

text=Label(window,text="Radius",fg="red")
text1=Entry(window)
text1.place(x=200,y=90)
text.place(x=100,y=90)

def area():
    Radius=float(text1.get())
    Area=22/7*(Radius**2)
    Label(window,text=str(Area),fg="brown").place(x=100,y=200)



B=Button(window,text="calculate",command=area,fg="brown")
B.place(x=100,y=150)

C=Button(window,text="exit",command=lambda:exit(),fg="brown")
C.place(x=230,y=150)

window.mainloop()
