from tkinter import *
window=Tk()
window.geometry("400x300")
H=Label(window,text="Registration form",fg="green")
H.pack()


text=Label(window,text="First name",fg="brown")
text.pack()
text1=Entry(window).pack()


D=Label(window,text="Last name",fg="brown")
D.pack()
text1=Entry(window).pack()

A=Label(window,text="Email",fg="brown")
A.pack()
text1=Entry(window).pack()

E=Label(window,text="Password",fg="brown")
E.pack()
text1=Entry(window,show="*").pack()

F=Label(window,text="Confirm Password",fg="brown")
F.pack()
text1=Entry(window,show="*").pack()


B=Button(window,text="login",fg="brown")
B.pack()

C=Button(window,text="Cancel",fg="brown")
C.pack()

window.mainloop()