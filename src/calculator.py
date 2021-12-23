from tkinter import *
window=Tk()
window.geometry("400x300")
w=Label(window,text="calculator",fg="green")
w.grid(row=0,column=1)

A=Entry(window).grid(row=3,column=1)

B=Button(window,text="1",fg="black")
B.grid(row=5,column=0)

C=Button(window,text="2",fg="black")
C.grid(row=5,column=1)

D=Button(window,text="3",fg="black")
D.grid(row=5,column=2)

E=Button(window,text="4",fg="black")
E.grid(row=6,column=0)

f=Button(window,text="5",fg="black")
f.grid(row=6,column=1)

g=Button(window,text="6",fg="black")
g.grid(row=6,column=2)

H=Button(window,text="7",fg="black")
H.grid(row=7,column=0)

i=Button(window,text="8",fg="black")
i.grid(row=7,column=1)

j=Button(window,text="9",fg="black")
j.grid(row=7,column=2)

k=Button(window,text="0",fg="black")
k.grid(row=8,column=1)

l=Button(window,text="X",fg="blue")
l.grid(row=8,column=2)

m=Button(window,text="%",fg="blue")
m.grid(row=8,column=0)

N=Button(window,text="+",fg="blue")
N.grid(row=5,column=3)

o=Button(window,text="-")
o.grid(row=6,column=3)

p=Button(window,text="/")
p.grid(row=7,column=3)

q=Button(window,text="=")
q.grid(row=8,column=3)
window.mainloop()
