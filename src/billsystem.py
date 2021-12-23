from tkinter import *
window=Tk()
window.geometry("400x500")
H=Label(window,text="Billing Form")
H.place(x=150,y=30)

D=Label(window,text="bill number:")
D.place(x=100,y=60)

text=Label(window,text="Customer name")
text1=Entry(window).place(x=200,y=90)
text.place(x=100,y=90)

A=Label(window,text="Address")
text2=Entry(window).place(x=200,y=110)
A.place(x=100,y=110)

E=Label(window,text="Item")
text3=Entry(window,width="20").place(x=50,y=190)
text4=Entry(window,width="20").place(x=50,y=210)

E.place(x=50,y=160)

F=Label(window,text="Qantity")
text5=Entry(window,width="10").place(x=155,y=190)
text6=Entry(window,width="10").place(x=155,y=210)

F.place(x=155,y=160)

G=Label(window,text="Rate")
text7=Entry(window,width="10").place(x=210,y=190)
text8=Entry(window,width="10").place(x=210,y=210)
G.place(x=210,y=160)

i=Label(window,text="Total")
text10=Entry(window,width="10").place(x=210,y=380)
i.place(x=210,y=350)
window.mainloop()