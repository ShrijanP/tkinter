from tkinter import *
window=Tk()
window.geometry("400x500")
window.title("BMI")
H=Label(window,text="BMI",fg="blue")
H.place(x=150,y=30)

text=Label(window,text="KG",fg="red")
text1=Entry(window)
text1.place(x=200,y=90)
text.place(x=100,y=90)

A=Label(window,text="HEIGHT",fg="red")
text2=Entry(window)
text2.place(x=200,y=110)
A.place(x=100,y=110)

def BMI():
    KGS=int(text1.get())
    htg=float(text2.get())
    BMI=KGS/(htg**2)
    Label(window,text=str(BMI),fg="brown").place(x=100,y=180)



B=Button(window,text="calculate",command=BMI,fg="red")
B.place(x=100,y=150)

C=Button(window,text="exit",command=lambda:exit(),fg="red")
C.place(x=230,y=150)

window.mainloop()
