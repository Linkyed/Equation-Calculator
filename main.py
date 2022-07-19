import tkinter as tk
import customtkinter as ck
from tkinter import messagebox

numbers_left = []
x_pos = 50
y_pos = 30
equation = []

#Function to save the number that the user typed, it can show if the user typed anything that is not a number too
def save_number():
    num = number_box.get()
    try:
        num = int(num)
        numbers_left.append(num)
        equation.append(num)
        print(numbers_left)
        equationLabel.set(equation)
        number_box.set('')
        
    except:
        messagebox.showinfo("Alert!", 'Please, only type number here')
        number_box.set('')
        
#The TK GUI start
ck.set_appearance_mode('dark')
ck.set_default_color_theme('green')
app = ck.CTk()
app.title("Equation Calculator")
app.geometry('200x200')

#String variable to use in the GUI
equationLabel = tk.StringVar()
equationLabel.set('0')
number_box = tk.StringVar()
number_box.set('0')


#Label that will show the equation that the user is creating
label = ck.CTkLabel(app, textvariable=equationLabel, corner_radius=10, fg_color=('grey20')).place(x=35, y=30)


#Just a frame that will be under the buttons and boxes
frame = ck.CTkFrame(app, width=191, height=100, corner_radius=10)
frame.place(x=x_pos-45, y=y_pos+34)


#Text box to the user type a numebert that he want to add
entry_box = ck.CTkEntry(app, background='grey', textvariable=number_box, width=80, height=1)
entry_box.place(x=x_pos+20, y=y_pos+40)



#Button for the operations
plus = ck.CTkButton(app, text="+")
plus.place(x=x_pos-10, y=y_pos+40)
plus.set_dimensions(26, 20)
minus = ck.CTkButton(app, text="-")
minus.place(x=x_pos-10, y=y_pos+62)
minus.set_dimensions(26, 20)
multiply = ck.CTkButton(app, text="*")
multiply.place(x=x_pos-10, y=y_pos+83.5)
multiply.set_dimensions(26, 20)
division = ck.CTkButton(app, text="/")
division.place(x=x_pos-10, y=y_pos+105)
division.set_dimensions(26, 20)

exponentation = ck.CTkButton(app, text="²")
exponentation.place(x=x_pos-37, y=y_pos+40)
exponentation.set_dimensions(26, 20)
square_root = ck.CTkButton(app, text="√")
square_root.place(x=x_pos-37, y=y_pos+62)
square_root.set_dimensions(26, 10)
start_paren = ck.CTkButton(app, text="(")
start_paren.place(x=x_pos-37, y=y_pos+83.5)
start_paren.set_dimensions(26, 20)
end_paren = ck.CTkButton(app, text=")")
end_paren.place(x=x_pos-37, y=y_pos+105)
end_paren.set_dimensions(26, 20)


#Button to the user save the number that he typed and add it to the equation
ck.CTkButton(app, text="💾", background='grey', height=1, width=1, command=save_number).place(x=x_pos+105, y=y_pos+40)

app.mainloop()

