from tkinter import *
root=Tk()
root.title("Welcome from Interest Calculator")
root.geometry("400x150")


def calculate():
    princ=int(text2.get())
    rate=int(text3.get())
    time=int(text4.get())
    amount=(princ*rate*time)/100
    l1=Label(root,text=str(amount),fg="brown").grid(row=6,column=5)

t2=Label(root,text="Interest: ",fg="blue")
t2.grid(row=6,column=4)

text1=Label(root,text="calculator",fg="red")
text1.grid(row=1,column=5)

text=Label(root,text="Principle",fg="red")
text2=Entry(root,)
text2.grid(row=3,column=5)
text.grid(row=3,column=3)

D=Label(root,text=" Rate",fg="red")
text3=Entry(root)
text3.grid(row=4,column=5)
D.grid(row=4,column=3)


A=Label(root,text="Time",fg="red")
text4=Entry(root)
text4.grid(row=5,column=5)
A.grid(row=5,column=3)



B=Button(root,text="Calculate",command=calculate,fg="red")
B.grid(row=3,column=8)

C=Button(root,text="Exit",command=lambda:exit(), fg="red")
C.grid(row=4,column=8)



root.mainloop()
