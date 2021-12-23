from tkinter import *
window=Tk()
window.geometry("400x300")
text=Label(window,text="Log in system",fg="brown")
text.pack()


text=Label(window,text="User name",fg="brown")
text.pack()
text1=Entry(window).pack()

A=Label(window,text="Password",fg="brown")
A.pack()
text1=Entry(window,show="*",).pack()


B=Button(window,text="login",fg="brown")
B.pack()
window.mainloop()