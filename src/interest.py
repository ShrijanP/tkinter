from tkinter import *
root=Tk()
root.title("Interest calculator")
root.geometry("300x150")

def calculate():
    princ=int(input(text2.get()))
    rate=int(input(text3.get()))
    time=int(input(text4.get()))
    amount=(princ*rate*time)/100
    Label(root,text={amount},fg="brown").grid(row=6,column=5)



text1=Label(root,text="calculator",fg="brown")
text1.grid(row=1,column=5)

text=Label(root,text="Principle",fg="brown")
text2=Entry(root).grid(row=3,column=5)
text.grid(row=3,column=3)

D=Label(root,text=" Rate",fg="brown")
text3=Entry(root).grid(row=4,column=5)
D.grid(row=4,column=3)


A=Label(root,text="Time",fg="brown")
text4=Entry(root).grid(row=5,column=5)
A.grid(row=5,column=3)

B=Button(root,text="Calculate",command=calculate,fg="Brown")
B.grid(row=3,column=8)

C=Button(root,text="Exit",command=lambda:exit(), fg="brown")
C.grid(row=4,column=8)
root.mainloop()
