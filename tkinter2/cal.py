from tkinter import *
window=Tk()
window.title(" welcome to Calculator")
window.geometry("480x350")
w=Label(window,text="welcome to calculator",fg="red")
w.grid(row=0,column=2)

A=Entry(window,width=55,borderwidth=5)
A.grid(row=2,column=0,columnspan=3 ,padx=10,pady=10)

def button_click(number):
    current=A.get()
    A.delete(0,END)
    A.insert(0,str(current)+str(number))



def button_add():
    first_number=A.get()
    global f_num
    f_num=int(first_number)
    A.delete(0,END)

def Button_equal():
    global f_num
    result = str(eval(f_num)) 
    A.set(result)
    expression = ""

def bt_clear(): 
    global f_num 
    expression = "" 
    A.set("")
 


B=Button(window,text="1",fg="red",padx=40,pady=20,command=lambda:button_click(1))
B.grid(row=5,column=0)

C=Button(window,text="2",fg="red",padx=40,pady=20,command=lambda:button_click(2))
C.grid(row=5,column=1)

D=Button(window,text="3",fg="red",padx=40,pady=20,command=lambda:button_click(3))
D.grid(row=5,column=2)

E=Button(window,text="4",fg="red",padx=40,pady=20,command=lambda:button_click(4))
E.grid(row=6,column=0)

f=Button(window,text="5",fg="red",padx=40,pady=20,command=lambda:button_click(5))
f.grid(row=6,column=1)

g=Button(window,text="6",fg="red",padx=40,pady=20,command=lambda:button_click(6))
g.grid(row=6,column=2)

H=Button(window,text="7",fg="red",padx=40,pady=20,command=lambda:button_click(7))
H.grid(row=7,column=0)

i=Button(window,text="8",fg="red",padx=40,pady=20,command=lambda:button_click(8))
i.grid(row=7,column=1)

j=Button(window,text="9",fg="red",padx=40,pady=20,command=lambda:button_click(9))
j.grid(row=7,column=2)

k=Button(window,text="0",fg="red",padx=40,pady=20,command=lambda:button_click(0))
k.grid(row=8,column=1)

l=Button(window,text="=",command=lambda:Button_equal(),fg="red",padx=40,pady=20)
l.grid(row=8,column=2)

m=Button(window,text="Clear",command=lambda:bt_clear(),fg="red",padx=40,pady=20)
m.grid(row=8,column=0)

N=Button(window,text="+",command=lambda:button_click("+"),fg="red",padx=40,pady=20)
N.grid(row=5,column=3)

o=Button(window,text="-",command=lambda:button_click("-"),fg="red",padx=40,pady=20)
o.grid(row=6,column=3)
p=Button(window,text="/",command=lambda:button_click("/"),fg="red",padx=40,pady=20)
p.grid(row=7,column=3)

q=Button(window,text="x",command=lambda:button_click("x"),fg="red",padx=40,pady=20)
q.grid(row=8,column=3)


window.mainloop()
