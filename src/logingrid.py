from tkinter import *
window=Tk()
window.geometry("400x300")
text=Label(window,text="Log in system",fg="brown")
text.grid(row=0,column=3)


text=Label(window,text="User name",fg="brown")
text1=Entry(window).grid(row=2,column=3)
text.grid(row=2,column=2)


A=Label(window,text="Password",fg="brown")
text1=Entry(window,show="*",).grid(row=3,column=3)
A.grid(row=3,column=2)


B=Button(window,text="login",fg="brown")
B.grid(row=4,column=2)

C=Button(window,text="cancel",fg="brown")
C.grid(row=4,column=3)
window.mainloop()
