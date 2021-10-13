from tkinter import *

gui = Tk()
gui.configure(background="black")
gui.title("Calculator")
gui.geometry("400x200")
var=StringVar()
result = " "
def clear():
        global result
        result =""
        var.set("")
def press(num):
        global result
        result = result + str(num)
        equation.set(result)
def equalpress():
        try:
            global result
            total = str(eval(result))
            var.set(total)
            result = ""
        except:
            var.set('error')
            result = ""




equation = StringVar()
entrresults=Entry(gui,text=equation,width=20,font=('Arial',20))
entrresults.grid(columnspan=4)

button1 = Button(gui,text='1', fg='black',bg='white',
        command=lambda: press(1),width=10, font=('Arial',12))
button1.grid(row=2, column=1)


button2 = Button(gui,text='2', fg='black',bg='white',
        command=lambda: press(2),width=10, font=('Arial',12))
button2.grid(row=2, column=2)


button3 = Button(gui,text='3', fg='black',bg='white',
        command=lambda: press(3),width=10, font=('Arial',12))
button3.grid(row=2, column=3)


button4 = Button(gui,text='4', fg='black',bg='white',
        command=lambda: press(4),width=10, font=('Arial',12))
button4.grid(row=3, column=1)


button5 = Button(gui,text='5', fg='black',bg='white',
        command=lambda: press(5),width=10, font=('Arial',12))
button5.grid(row=3, column=2)


button6 = Button(gui,text='6', fg='black',bg='white',
        command=lambda: press(6),width=10, font=('Arial',12))
button6.grid(row=3, column=3)


button7 = Button(gui,text='7', fg='black',bg='white',
        command=lambda: press(7),width=10, font=('Arial',12))
button7.grid(row=4, column=1)


button8 = Button(gui,text='8', fg='black',bg='white',
        command=lambda: press(8),width=10, font=('Arial',12))
button8.grid(row=4, column=2)


button9 = Button(gui,text='9', fg='black',bg='white',
        command=lambda: press(9),width=10, font=('Arial',12))
button9.grid(row=4, column=3)


button0 = Button(gui,text='1', fg='black',bg='white',
        command=lambda: press(0),width=10, font=('Arial',12))
button0.grid(row=5, column=1)


Clear = Button(gui,text='Clear', fg='black',bg='white',
        command=clear, width=10, font=('Arial',12))
Clear.grid(row=5, column=2)


equels = Button(gui,text='=', fg='black',bg='red',
        command=equalpress, width=10, font=('Arial',12))
equels.grid(row=5, column=3)


dieresi= Button(gui,text='/', fg='black',bg='red',
        command=lambda: press('/'), width=10, font=('Arial',12))
dieresi.grid(row=5, column=4)


times = Button(gui,text='*', fg='black',bg='red',
        command=lambda: press('+'), width=10, font=('Arial',12))
times.grid(row=4, column=4)


mion= Button(gui,text='-', fg='black',bg='red',
        command=lambda: press('-'), width=10, font=('Arial',12))
mion.grid(row=3, column=4)


plus = Button(gui,text='+', fg='black',bg='red',
        command=lambda: press('+'), width=10, font=('Arial',12))
plus.grid(row=2, column=4)


dot = Button(gui,text='.', fg='black',bg='red',
        command=lambda: press('.'), width=10, font=('Arial',12))
dot.grid(row=6, column=1)

gui.mainloop()