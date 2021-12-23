from tkinter import *
window=Tk()
window.geometry("400x300")
H=Label(window,text="Registration form",fg="green")
H.grid(row=1,column=5)


text=Label(window,text="First name",fg="brown")
text1=Entry(window).grid(row=3,column=5)
text.grid(row=3,column=3)

D=Label(window,text="Last name",fg="brown")
text1=Entry(window).grid(row=4,column=5)
D.grid(row=4,column=3)


A=Label(window,text="Email",fg="brown")
text1=Entry(window).grid(row=5,column=5)
A.grid(row=5,column=3)

E=Label(window,text="Password",fg="brown")
text1=Entry(window,show="*").grid(row=6,column=5)
E.grid(row=6,column=3)

F=Label(window,text="Confirm Password",fg="brown")
text1=Entry(window,show="*").grid(row=7,column=5)
F.grid(row=7,column=3)


B=Button(window,text="login",fg="brown")
B.grid(row=8,column=3)

C=Button(window,text="Cancel",fg="brown")
C.grid(row=8,column=5)
window.mainloop()