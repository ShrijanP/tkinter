from tkinter import *
window=Tk()
window.geometry("400x300")
text=Label(window,text="User name",fg="brown")
text1=Entry(window).place(x=180,y=50)
text.place(x=100,y=50)


A=Label(window,text="Password",fg="brown")
text1=Entry(window,show="*",).place(x=180,y=90)
A.place(x=100,y=90)


B=Button(window,text="login",fg="brown")
B.place(x=150,y=120)

C=Button(window,text="cancel",fg="brown")
C.place(x=200,y=120)

window.mainloop()