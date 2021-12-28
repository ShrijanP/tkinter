from tkinter import *
window=Tk()
window.geometry("400x300")
text=Label(window,text="welcome to Log in system",fg="Red")
text.grid(row=0,column=3)


text=Label(window,text="User name",fg="brown")
text1=Entry(window)
text1.grid(row=2,column=3)
text.grid(row=2,column=2)


A=Label(window,text="Password",fg="brown")
text2=Entry(window,show="*",).grid(row=3,column=3)
A.grid(row=3,column=2)


def click():
    output="your user name is :"+text1.get()
    mylabel=Label(window,text=output,fg="brown")
    mylabel.grid(row=7,column=3)

B=Button(window,text="login",command=click,fg="brown")
B.grid(row=4,column=2)

C=Button(window,text="Exit",command=lambda:exit(),fg="brown")
C.grid(row=4,column=3)




window.mainloop()
