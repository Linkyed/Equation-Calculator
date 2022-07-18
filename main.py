import tkinter as tk

number = []

#Function to use in the TK buttons, just add and erase numbers for now
def add_1():
    number.append(1)
    string = ''
    for iten in number:
        string = string + str(iten)
    textV.set(string)
def add_2():
    number.append(2)
    string = ''
    for iten in number:
        string = string + str(iten)
    textV.set(string)
def add_3():
    number.append(3)
    string = ''
    for iten in number:
        string = string + str(iten)
    textV.set(string)
def add_4():
    number.append(4)
    string = ''
    for iten in number:
        string = string + str(iten)
    textV.set(string)
def add_5():
    number.append(5)
    string = ''
    for iten in number:
        string = string + str(iten)
    textV.set(string)
def add_6():
    number.append(6)
    string = ''
    for iten in number:
        string = string + str(iten)
    textV.set(string)
def add_7():
    number.append(7)
    string = ''
    for iten in number:
        string = string + str(iten)
    textV.set(string)
def add_8():
    number.append(8)
    string = ''
    for iten in number:
        string = string + str(iten)
    textV.set(string)
def add_9():
    number.append(9)
    string = ''
    for iten in number:
        string = string + str(iten)
    textV.set(string)
def add_0():
    number.append(0)
    string = ''
    for iten in number:
        string = string + str(iten)
    textV.set(string)
def backspace():
    number.pop()
    string = ''
    for iten in number:
        string = string + str(iten)
    print(number)
    textV.set(string)


#The TK GUI start
app = tk.Tk()

app.title("Equation Calculator")
app.geometry('200x200')
textV = tk.StringVar()
textV.set('0')

#Label that will show the equation that the user is creating
equation = tk.Label(app, textvariable=textV ).place(x=100, y=10)

#Button for the numbers
tk.Button(app, text="1", background='grey', height=1, width=1, command=add_1).place(x=100, y=50)
tk.Button(app, text="2", background='grey', height=1, width=1, command=add_2).place(x=120, y=50)
tk.Button(app, text="3", background='grey', height=1, width=1, command=add_3).place(x=140, y=50)
tk.Button(app, text="4", background='grey', height=1, width=1, command=add_4).place(x=100, y=80)
tk.Button(app, text="5", background='grey', height=1, width=1, command=add_5).place(x=120, y=80)
tk.Button(app, text="6", background='grey', height=1, width=1, command=add_6).place(x=140, y=80)
tk.Button(app, text="7", background='grey', height=1, width=1, command=add_7).place(x=100, y=110)
tk.Button(app, text="8", background='grey', height=1, width=1, command=add_8).place(x=120, y=110)
tk.Button(app, text="9", background='grey', height=1, width=1, command=add_9).place(x=140, y=110)
tk.Button(app, text="0", background='grey', height=1, width=1, command=add_0).place(x=120, y=140)

#Button for the operations
tk.Button(app, text="+", background='grey', height=1, width=1).place(x=80, y=50)
tk.Button(app, text="-", background='grey',height=1, width=1).place(x=80, y=80)
tk.Button(app, text="*", background='grey', height=1, width=1).place(x=80, y=110)
tk.Button(app, text="/", background='grey', height=1, width=1).place(x=80, y=140)
tk.Button(app, text="²", background='grey', height=1, width=1).place(x=60, y=50)
tk.Button(app, text="√", background='grey',height=1, width=1).place(x=60, y=80)
tk.Button(app, text="(", background='grey', height=1, width=1).place(x=60, y=110)
tk.Button(app, text=")", background='grey', height=1, width=1).place(x=60, y=140)

#Button for backspace action
tk.Button(app, text='⌫', background='grey', height=1, width=1, command=backspace).place(x=160, y=50)

app.mainloop()

