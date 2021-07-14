from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mx
import parser as pr
win = Tk()
win.title("Calculator")
win.wm_iconbitmap('1.ico')
win.configure(bg='#212623')
def function():
    mx.showinfo(title='Raut Calculator', message='Name: Calc BCC\'s\nCreator: WINNAR')

def lamb():
    mx.showinfo(title='Help', message="Please Press the button to calculate")
mainmenu = Menu(win)
submenu = Menu(mainmenu, tearoff=False)
mainmenu.add_cascade(label='About', command=function)
mainmenu.add_cascade(label='Help', command=lamb)

index = 0
def exper(i):
    global index
    entry1.insert(index, i)
    index+=1

def func():
    entry1.delete(0, END)

def func1():
    capture = entry1.get()
    if len(capture):
        new_capture = capture[:-1]
        func()
        entry1.insert(0, new_capture)

def operation(operator):
    global index
    length = len(operator)
    entry1.insert(index, operator)
    index+=length

def result():
    string1 = entry1.get()
    try:
        a = pr.expr(string1).compile()
        b = eval(a)
        func()
        entry1.insert(0, b)
    except Exception:
        func()
        entry1.insert(0, 'Error')

entry1 = Entry(win, fg='white', bg='#212623', font='15')
entry1.pack(side=TOP, fill=X, ipadx=5, ipady=15)



label1 = Label(win, bg='#212623')
label1.pack(side=TOP, fill=X)

button1 = Button(label1, text='ON', height=2, width=7, font='10', fg='white', bg='green')
button1.grid(row=1, column=0, padx=0, pady=0)

button2 = Button(label1, text='OFF', height=2, width=7, font='10', fg='white', bg='red', command=win.destroy)
button2.grid(row=1, column=1, padx=0, pady=0)

button3 = Button(label1, text='C', height=2, width=7, font='10', fg='white', bg='#212623', command=func)
button3.grid(row=1, column=2, padx=0, pady=0)


button4 = Button(label1, text='⬅', height=2, width=7, font='10', fg='white', bg='#212623', command=func1)
button4.grid(row=1, column=3, padx=0, pady=0)


button5 = Button(label1, text='pi', height=2, width=7, font='10', fg='white', bg='#212623', command=lambda : operation('3.14'))
button5.grid(row=2, column=0, padx=0, pady=0)


button6 = Button(label1, text='x^2', height=2, width=7, font='10', fg='white', bg='#212623', command=lambda : operation('**2'))
button6.grid(row=2, column=1, padx=0, pady=0)


button7 = Button(label1, text='x^1/2', height=2, width=7, font='10', fg='white', bg='#212623', command=lambda : operation('**1/2'))
button7.grid(row=2, column=2, padx=0, pady=0)


button8 = Button(label1, text='➗', height=2, width=7, font='10', fg='white', bg='#212623', command=lambda : operation('/'))
button8.grid(row=2, column=3, padx=0, pady=0)


button9= Button(label1, text='7', height=2, width=7, font='10', bg='#000', fg='white', command=lambda : exper(7))
button9.grid(row=3, column=0, padx=0, pady=0)


button10= Button(label1, text='8', height=2, width=7, font='10', bg='#000', fg='white', command=lambda : exper(8))
button10.grid(row=3, column=1, padx=0, pady=0)


button11= Button(label1, text='9', height=2, width=7, font='10', bg='#000', fg='white', command=lambda : exper(9))
button11.grid(row=3, column=2, padx=0, pady=0)


button12 = Button(label1, text='✖', height=2, width=7, font='10', fg='white', bg='#212623', command=lambda : operation('*'))
button12.grid(row=3, column=3, padx=0, pady=0)


button13= Button(label1, text='4', height=2, width=7, font='10', bg='#000', fg='white', command=lambda : exper(4))
button13.grid(row=4, column=0, padx=0, pady=0)


button14= Button(label1, text='5', height=2, width=7, font='10', bg='#000', fg='white', command=lambda : exper(5))
button14.grid(row=4, column=1, padx=0, pady=0)


button= Button(label1, text='6', height=2, width=7, font='10', bg='#000', fg='white', command=lambda : exper(6))
button.grid(row=4, column=2, padx=0, pady=0)


button15 = Button(label1, text='➖', height=2, width=7, font='10', bg='#212623', fg='white', command=lambda : operation("-"))
button15.grid(row=4, column=3, padx=0, pady=0)


button16= Button(label1, text='1', height=2, width=7, font='10', bg='#000', fg='white', command=lambda : exper(1))
button16.grid(row=5, column=0, padx=0, pady=0)


button17= Button(label1, text='2', height=2, width=7, font='10', bg='#000', fg='white', command=lambda : exper(2))
button17.grid(row=5, column=1, padx=0, pady=0)


button18= Button(label1, text='3', height=2, width=7, font='10', bg='#000', fg='white', command=lambda : exper(3))
button18.grid(row=5, column=2, padx=0, pady=0)


button19 = Button(label1, text='➕', height=2, width=7, font='10', fg='white', bg='#212623', command=lambda : operation('+'))
button19.grid(row=5, column=3, padx=0, pady=0)



button20 = Button(label1, text='g', height=2, width=7, font='10', fg='white', bg='black', command=lambda : exper('9.8'))
button20.grid(row=6, column=0, padx=0, pady=0)


button21 = Button(label1, text='0', height=2, width=7, font='10', fg='white', bg='black', command=lambda : exper(0))
button21.grid(row=6, column=1, padx=0, pady=0)


button22 = Button(label1, text='.', height=2, width=7, font='10', fg='white', bg='black', command=lambda : exper('.'))
button22.grid(row=6, column=2, padx=0, pady=0)


button23 = Button(label1, text='=', height=2, width=7, font='10', fg='white', bg='#080ea6', command=lambda : result())
button23.grid(row=6, column=3, padx=0, pady=0)

win.config(menu=mainmenu)
win.mainloop()

