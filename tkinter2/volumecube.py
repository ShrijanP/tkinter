from tkinter import *
window=Tk()
window.geometry("400x300")
window.title("perform volume of cube")

H=Label(window,text="perform volume of cube",fg="brown")
H.place(x=150,y=30)

text=Label(window,text="length",fg="red")
text1=Entry(window)
text1.place(x=200,y=90)
text.place(x=100,y=90)

def Volume():
    len=float(text1.get())
    VOlume=(len)**3
    Label(window,text=str(VOlume),fg="red").place(x=100,y=200)



B=Button(window,text="calculate",command=Volume,fg="red")
B.place(x=100,y=150)

C=Button(window,text="exit",command=lambda:exit(),fg="Brown")
C.place(x=230,y=150)

window.mainloop()
