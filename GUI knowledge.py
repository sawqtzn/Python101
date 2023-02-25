from tkinter import *
from tkinter import ttk #theme of tk
from tkinter import messagebox

GUI = Tk() # นี่คือหน้าจอหลักของโปรแกรม
GUI.title('my diary') # ชื่อโปรแกรม
GUI.geometry('500x400') # ขนาดโปรแกรม

L1 = Label(GUI,text='My diary',font=('Angsana New',25),fg='#FAAFBA')
L1.place(x=30,y=20)
###################
def Button1():
    text='Hi my name is Supanan. I wad born since 2007. Nice to meet you guys!'
    messagebox.showinfo('About me',text)

FB1 = Frame(GUI) # คล้ายกระดาน
FB1.place(x=100,y=80)
B1 = Button(FB1,text='About me',command=Button1)
B1.pack(ipadx=15,ipady=7)
###################
def Button2():
    text='Today I recieved so many flowers from my friends. They are so lovely.'
    messagebox.showinfo('Diary 14/02/2023',text)

FB2 = Frame(GUI) # คล้ายกระดาน
FB2.place(x=100,y=80)
B2 = Button(FB1,text='Read my latest diary',command=Button2)
B2.pack(ipadx=15,ipady=7)
###################
def Button3():
    text='oops error! Pls contact the owner of this diary'
    messagebox.showerror('Pls select the date',text)

FB3 = Frame(GUI) # คล้ายกระดาน
FB3.place(x=100,y=80)
B3 = Button(FB1,text='read my diary',command=Button3)
B3.pack(ipadx=15,ipady=7)
###################
def Button4():
    text='Pls wait 12-13days for the author to respond'
    messagebox.showinfo('inform the author',text)

FB4 = Frame(GUI) # คล้ายกระดาน
FB4.place(x=100,y=80)
B4 = Button(FB1,text='contact the author',command=Button4)
B4.pack(ipadx=15,ipady=7)


GUI.mainloop()
